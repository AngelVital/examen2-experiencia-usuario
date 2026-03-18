import re

def process_file():
    with open('index.html', 'r', encoding='utf-8') as f:
        idx_content = f.read()
    with open('articulo.html', 'r', encoding='utf-8') as f:
        art_content = f.read()

    idx_style = re.search(r'<style>(.*?)</style>', idx_content, re.DOTALL).group(1)
    art_style = re.search(r'<style>(.*?)</style>', art_content, re.DOTALL).group(1)

    # get article specific CSS
    art_specific = ''
    if '/* ARTICLE SPECIFIC STYLES */' in art_style:
        art_specific = '/* ARTICLE SPECIFIC STYLES */\n' + art_style.split('/* ARTICLE SPECIFIC STYLES */')[1]

    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(idx_style + '\n' + art_specific)

    script_content = '''function toggleMenu() {
    const sidebar = document.getElementById('sidebarMenu');
    const backdrop = document.querySelector('.menu-backdrop');

    sidebar.classList.toggle('active');
    backdrop.classList.toggle('active');
}'''
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(script_content)

    idx_clean = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="styles.css">', idx_content, flags=re.DOTALL)
    idx_clean = re.sub(r'<script>.*?</script>', '<script src="script.js"></script>', idx_clean, flags=re.DOTALL)

    art_clean = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="styles.css">', art_content, flags=re.DOTALL)
    art_clean = re.sub(r'<script>.*?</script>', '<script src="script.js"></script>', art_clean, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx_clean)
    with open('articulo.html', 'w', encoding='utf-8') as f:
        f.write(art_clean)

if __name__ == '__main__':
    process_file()
