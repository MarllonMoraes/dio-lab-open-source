from PIL import Image

def grayscale(image_path):
  """Converte uma imagem para escala de cinza.

  Args:
    image_path: Caminho para a imagem.
  """
  img = Image.open(image_path).convert('L')
  img.save(f"{image_path[:-4]}_grayscale.jpg")

def resize(image_path, width, height):
  """Redimensiona uma imagem.

  Args:
    image_path: Caminho para a imagem.
    width: Nova largura.
    height: Nova altura.
  """
  img = Image.open(image_path)
  img_resized = img.resize((width, height))
  img_resized.save(f"{image_path[:-4]}_resized.jpg")