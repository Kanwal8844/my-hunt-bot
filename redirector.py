from flask import Flask, redirect, request

app = Flask(__name__)

# آپ کا CPA جال
CPA_LINK = "https://playabledownload.com/1897723"

@app.route('/')
def intercept():
    # یہاں کوڈ یہ دیکھتا ہے کہ آیا "سمندر" (سورس) سے کوئی غلط ڈیٹا (Parameter) آیا ہے؟
    # اگر ویب سائٹ خود یوزر کو ری ڈائریکٹ کر رہی ہے، تو ہم اسے پکڑ لیں گے
    incoming_data = request.args.to_dict()
    
    if incoming_data:
        # یہ لاگ ہمیں بتائے گا کہ ویب سائٹ کہاں غلطی کر رہی ہے
        print(f"[!] سمندر کی غلطی پکڑی گئی! ڈیٹا: {incoming_data}")
        return redirect(CPA_LINK)
    
    return "سسٹم آن لائن ہے..."

if __name__ == '__main__':
    app.run(port=5000)