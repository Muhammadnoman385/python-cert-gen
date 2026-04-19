import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

def generate_certificates():
    output_dir = "certificates"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        
        df = pd.read_csv("data.csv")
        
        font_path = "font.ttf"
        
        
        template_path = "template.png" 
        
        if not os.path.exists(template_path):
            print(f"Error: Template file '{template_path}' nahi mili!")
            return

        for index, row in df.iterrows():
            # iloc[0] = Name, iloc[1] = Department
            name = str(row.iloc[0]).strip()
            dept = str(row.iloc[1]).strip()
            
            if name.lower() == "nan" or not name: continue

            img = Image.open(template_path)
            draw = ImageDraw.Draw(img)
            w_img, h_img = img.size

            # Font colors (dark blue/black mix)
            text_color = "#2c3e50"

            # --- NAME PRINT ---
            font_name = ImageFont.truetype(font_path, 42) # Font size barhaya
            bbox_n = draw.textbbox((0, 0), name, font=font_name)
            w_n = bbox_n[2] - bbox_n[0]
            
            # --- NAME POSITION ADJUSTMENT ---
          
            text_n_y_position = 250
            
            
            pos_name = ((w_img - w_n) / 2 + 65, text_n_y_position) 
            draw.text(pos_name, name, fill=text_color, font=font_name)

            # --- DEPARTMENT PRINT ---
            font_dept = ImageFont.truetype(font_path, 32)
            bbox_d = draw.textbbox((0, 0), dept, font=font_dept)
            w_d = bbox_d[2] - bbox_d[0]
            
           
            text_d_y_position = 390
            
           
            pos_dept = ((w_img - w_d) / 2 + 85, text_d_y_position)
            draw.text(pos_dept, dept, fill=text_color, font=font_dept)

            # Save
            file_name = f"{output_dir}/{name.replace(' ', '_')}.png"
            img.save(file_name)
            print(f"Success: {name}")
            
        print("\nSaare certificates naye template ke mutabiq ready hain!")
            
    except Exception as e:
        print(f"Final Error: {e}")

if __name__ == "__main__":
    generate_certificates()