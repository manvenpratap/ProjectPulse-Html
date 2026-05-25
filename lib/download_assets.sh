#!/bin/bash

# Setup directories
LIB_DIR="$(pwd)"
cd "$LIB_DIR"

echo "Downloading Phosphor Icons package..."
curl -sL "https://registry.npmjs.org/@phosphor-icons/web/-/web-2.1.1.tgz" -o phosphor.tgz

echo "Extracting Phosphor Icons..."
tar -xzf phosphor.tgz
rm phosphor.tgz

# Rename package to phosphor
rm -rf phosphor
mv package phosphor

echo "Downloading Google Fonts CSS..."
FONTS_URL="https://fonts.googleapis.com/css2?family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&family=Fraunces:ital,opsz,wght@0,9..144,100..900;1,9..144,100..900&family=Inter:wght@100..900&family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&family=Nunito:ital,wght@0,200..1000;1,200..1000&family=Orbitron:wght@400..900&family=Outfit:wght@100..900&family=Paytone+One&family=Rajdhani:wght@300;400;500;600;700&family=Satoshi:wght@300;400;500;700;900&family=Work+Sans:wght@300;400;500;600;700&display=swap"

# Pretend to be a modern browser to get the woff2 files
USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

mkdir -p fonts
curl -sL -A "$USER_AGENT" "$FONTS_URL" -o temp-google-fonts.css

echo "Downloading individual font files..."
# Extract all url(...) links that point to https://fonts.gstatic.com/
URLS=$(grep -oE 'https://fonts.gstatic.com/[^)]+' temp-google-fonts.css)

for url in $URLS; do
    filename=$(basename "$url")
    if [ ! -f "fonts/$filename" ]; then
        echo "Downloading font $filename..."
        curl -sL -A "$USER_AGENT" "$url" -o "fonts/$filename"
    fi
    # Replace the URL in the CSS with the local path
    sed -i '' "s|$url|./fonts/$filename|g" temp-google-fonts.css
done

mv temp-google-fonts.css google-fonts.css

echo "Done downloading offline assets!"
