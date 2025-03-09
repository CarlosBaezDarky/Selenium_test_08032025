from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

# Fixture para inicializar y cerrar el navegador
@pytest.fixture(scope="function")
def driver():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

# Función de prueba
def test_add_remove_elements(driver):
    try:
        # Abre la página
        driver.get("https://the-internet.herokuapp.com")
        print("Página abierta: https://the-internet.herokuapp.com")
        assert "The Internet" in driver.title

        # Espera a que la página cargue y encuentra el enlace "Add/Remove Elements"
        add_remove_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Add/Remove Elements"))
        )
        add_remove_link.click()
        print("Clic en 'Add/Remove Elements'")

        # Espera a que la página de "Add/Remove Elements" cargue
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Add Element']"))
        )

        # Encuentra el botón "Add Element" y haz clic en él
        add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
        add_button.click()
        print("Clic en 'Add Element'")

        # Espera a que el nuevo botón "Delete" aparezca
        delete_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Delete']"))
        )
        delete_button.click()
        print("Clic en 'Delete'")

        # Espera unos segundos para ver el resultado
        time.sleep(10)

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        raise e  # Relanza la excepción para que pytest la capture