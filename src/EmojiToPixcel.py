import cairo
import gi
gi.require_version('Pango', '1.0')
gi.require_version('PangoCairo', '1.0')
from gi.repository import Pango, PangoCairo
from PIL import Image
import io

def surface_to_pil(surface):
    """Cairo の ImageSurface を PIL Image に変換"""
    buf = io.BytesIO()
    surface.write_to_png(buf)
    buf.seek(0)
    return Image.open(buf)

def emoji_to_pixel_art_pango(emoji, output_size=128, pixel_size=32):
    # キャンバスサイズは出力サイズと同じ
    canvas_size = output_size
    # カラー情報を保持するため FORMAT_ARGB32 を使用
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas_size, canvas_size)
    ctx = cairo.Context(surface)
    
    # Pango レイアウトを作成
    layout = PangoCairo.create_layout(ctx)
    layout.set_text(emoji, -1)
    
    # フォントサイズを出力サイズの80％に設定して絵文字がはみ出さないようにする
    font_size = int(output_size * 0.6)
    font_desc = Pango.FontDescription(f"Segoe UI Emoji {font_size}")
    layout.set_font_description(font_desc)
    
    # レイアウトの描画領域を取得し、中央に配置
    _, logical_rect = layout.get_pixel_extents()
    x = (canvas_size - logical_rect.width) / 2 - logical_rect.x
    y = (canvas_size - logical_rect.height) / 2 - logical_rect.y
    ctx.move_to(x, y)
    
    # PangoCairo で描画（カラー情報もレンダリングされる）
    PangoCairo.show_layout(ctx, layout)
    
    # Cairo の Surface を PIL Image に変換
    img = surface_to_pil(surface)
    
    # ドット絵風に変換（低解像度に縮小→Nearest Neighbor で再拡大）
    img_small = img.resize((pixel_size, pixel_size), resample=Image.NEAREST)
    pixel_art = img_small.resize((output_size, output_size), resample=Image.NEAREST)
    
    return pixel_art

if __name__ == "__main__":
    emoji = input("絵文字を入力してください: ") # 変換したい絵文字
    code_points = [f"U+{ord(ch):04X}" for ch in emoji]
    print("絵文字の文字コード:", " ".join(code_points))
    pixel_art = emoji_to_pixel_art_pango(emoji)
    pixel_art.save(f"emoji_{code_points}.png")
    print("画像が 'emoji_pango.png' として保存されました。")
