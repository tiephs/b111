from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# # Cấu hình webdriver
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Chạy không hiển thị trình duyệt
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# Khởi tạo driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Truy cập trang web
driver.get("https://neymarsport.com/?srsltid=AfmBOoqW8z-BdC4BI_GYE2GpkVrF0OahypUqO35Tv9js7mTPB6v1Sd4o")
time.sleep(3)  # Đợi trang tải

# Lấy danh sách sản phẩm
products = driver.find_elements(By.CSS_SELECTOR, "div.item-info")

# Duyệt qua từng sản phẩm để lấy thông tin
data = []
for product in products:
    try:
        name = product.find_element(By.CSS_SELECTOR, ".product-name").text
        price = product.find_element(By.CSS_SELECTOR, ".price.product-price").text
        if name:
            data.append((name, price))
    except Exception as e:
        print("Lỗi khi lấy thông tin sản phẩm:", e)

# In dữ liệu ra màn hình
for item in data:
    print(f"Tên: {item[0]} - Giá: {item[1]}")

# Đóng trình duyệt
driver.quit()