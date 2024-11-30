# BankAccount 類別實現與單元測試

這個專案展示了一個簡單的 Python 類別 `BankAccount`，用於模擬銀行賬戶功能。包括存款、取款和查詢餘額等功能。並通過 `unittest` 庫進行單元測試。

## 目錄

- [BankAccount 類別](#bankaccount-類別)
- [單元測試](#單元測試)
- [使用方法](#使用方法)
- [設置與執行](#設置與執行)
- [日誌](#日誌)
- [貢獻](#貢獻)
- [授權](#授權)

## BankAccount 類別

`BankAccount` 類別包含以下功能：

- **屬性**
  - `account_holder`：賬戶持有者的姓名
  - `balance`：賬戶餘額

- **方法**
  - `display_balance()`：顯示當前賬戶餘額
  - `deposit(amount)`：存款
  - `withdraw(amount)`：取款

## 單元測試

使用 `unittest` 庫對 `BankAccount` 類別進行測試，包括初始餘額、存款、取款、餘額不足和無效存款等測試。

### 測試項目
- 初始餘額
- 存款
- 取款
- 餘額不足處理
- 無效存款處理

## 使用方法

1. 創建 `BankAccount` 類別的實例：
```python
my_account = BankAccount("Alice")
```
2. 存款：
```python
my_account.deposit(100)
```
3. 取款：
```python
my_account.withdraw(50)
```
4. 顯示餘額:
```python
my_account.display_balance()
```

## 設置與執行

1. 安裝 Python 3.7 或更新版本。
2. 克隆這個倉庫:
```bash
git clone <[bankaccount](https://github.com/Jc-0128/API/tree/main/bankaccount)>
```
3. 在專案目錄中創建和編輯 `bankaccount.py` 文件，並將 BankAccount 類別代碼複製到該文件中。
4. 在專案目錄中創建和編輯 `test.py` 文件，並將測試代碼複製到該文件中。
5. 執行測試：
```bash
python test.py
```

## 日誌
此程式使用 `logging` 模塊記錄賬戶操作，日誌級別設置為 `INFO`。

## 貢獻
歡迎貢獻！請提交拉取請求並說明更改內容。

## 授權
此專案基於 MIT 授權條款。詳情請參見 LICENSE 文件。
