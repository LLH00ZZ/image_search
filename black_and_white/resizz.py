from PIL import Image

path = "/home/shuchenweng/cz/llh/2025_1_16/old_film_project/T2I-Copilot-master/black_and_white/05340u.jpg"
img = Image.open(path).convert("RGB")
img = img.resize((464, 304), Image.LANCZOS)   # 宽464，高304，LANCZOS抗锯齿
img.save("05340u_304x464.jpg")
print("done -> 05340u_304x464.jpg")