# このコードについて

入力された絵文字を白黒のピクセルアートにするツールになります。  
使用しているライブラリの関係上、MSYS2を使用している為、  
MSYS2の環境がある方のみ使用してください。  
以下に実行環境を記載しておきますので、参考にしてください。  
また、以下の環境以外で動作させた場合、正常に動作しない可能性があります。  

# 実行環境  

- Windows側  
  - エディション：Windows 10 Home  
  - バージョン：22H2  
  - OS ビルド：19045.5679  
  - エクスペリエンス：Windows Feature Experience Pack 1000.19061.1000.0  

- MSYS2側  
  - msys2-runtime 3.5.7-4  
  - Python 3.12.9  

# 環境の構築

MSYS2が入っている前提で進めます。  
入っていない場合は[MSYS2]("https://www.msys2.org/")のサイトから環境構築を実施してください。  
このプログラムを作成した際に使用したインストーラーはmsys2-x86_64-20250221.exeになります。  

MSYS2 MINGW64を実行し、以下のコマンドでパッケージをインストールしてください。  

```bash
pacman -Syu
pacman -S mingw-w64-x86_64-python3-gobject mingw-w64-x86_64-cairo mingw-w64-x86_64-pango mingw-w64-x86_64-gtk3
```

インストールしたらPythonのファイルがあるフォルダまで移動し、pythonコマンドで実行してください。  
入力した文字がターミナル状は文字化けしますが、出力には問題ありません。  

**🐾の文字をピクセルアートとして出力する場合**  
コードを実行すると`絵文字を入力してください:`と出てくるので🐾を入力する。  
![image](https://github.com/user-attachments/assets/3821196b-61fd-4723-b86f-2c475afcea0a)  

入力したらそのままエンターを押してください。
Pythonのコードがあるフォルダ直下に画像ファイルが出力されます。
![image](https://github.com/user-attachments/assets/76b18a2c-5ea1-406d-8767-d671356f7381)


