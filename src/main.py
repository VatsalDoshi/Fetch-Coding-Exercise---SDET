from helpers import setup_driver
from algorithm import find_fake_bar

def main():
    driver = setup_driver()
    try:
        fake_bar = find_fake_bar(driver)
        print(f"The identified fake gold bar is: {fake_bar}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
