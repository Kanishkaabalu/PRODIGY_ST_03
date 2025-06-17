# PRODIGY_ST_03
# Automated Login Test for a Web Application

## ✅ Task Objective
Create a test suite using a library of your choice that automates testing the login functionality of a web application. The test should include:

- ✔️ Positive test case (valid credentials)
- ❌ Negative test cases (invalid credentials, empty fields)

---

## 🔧 Tech Stack Used

- **Language:** Python  
- **Library:** Selenium  
- **Browser:** Chrome  
- **Website Used for Testing:**  
  [Practice Test Login Page](https://practicetestautomation.com/practice-test-login/)

---

## 🧪 Test Scenarios

| Test Case ID | Description                         | Input                          | Expected Output                                  |
|--------------|-------------------------------------|--------------------------------|--------------------------------------------------|
| TC01         | Valid login                         | Username: `student`<br>Password: `Password123` | Redirect to success page                        |
| TC02         | Invalid password                    | Username: `student`<br>Password: `wrongpass`    | Error message displayed                         |
| TC03         | Invalid username                    | Username: `wronguser`<br>Password: `Password123`| Error message displayed                         |
| TC04         | Empty username                      | Username: *(empty)*<br>Password: `Password123`  | Error or validation message                     |
| TC05         | Empty password                      | Username: `student`<br>Password: *(empty)*      | Error or validation message                     |
| TC06         | Both fields empty                   | Username: *(empty)*<br>Password: *(empty)*      | Error or validation message 
|---

## 💻 Code: `login_test.py`
requirements.txt
selenium
