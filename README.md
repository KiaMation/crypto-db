# 📈 Cryptocurrency Price Tracker

## 📌 Overview
This project fetches real-time cryptocurrency prices from multiple sources and stores them in a JSON file. It is automated using **GitHub Actions** to update price data every 5 minutes.

## 🔍 Features
- 🔄 Fetches real-time prices for **BTC, ETH, and DOGE**.
- ⚡ Integrates with **CoinPaprika, CoinGecko, KuCoin, and Bitfinex**.
- ⌚ Automated updates via **GitHub Actions**.
- 📝 Saves price data locally in `prices.json`.
- 💡 Supports easy expansion for additional cryptocurrencies.

## ⚙️ Requirements
- 💻 Python **3.8+**
- 📝 GitHub repository with **Actions enabled**

## 🛠 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/crypto-price-tracker.git
cd crypto-price-tracker
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Script Locally
```sh
python update_prices.py
```
This will fetch and save the latest prices into `prices.json`.

## 📅 GitHub Actions - Automated Updates
This project includes a **GitHub Actions workflow** that automatically updates the price data every **5 minutes**.

### 🔄 Workflow Configuration
Located in `.github/workflows/update-prices.yml`, the workflow:
1. Runs on a **cron schedule** every 5 minutes (`*/5 * * * *`).
2. Fetches and updates price data.
3. Commits and pushes updates to the repository.

### 🛠 Setting Up GitHub Secrets
To enable auto-commit functionality, add a **GitHub Secret** named `TOKEN` in your repository settings. This token allows the workflow to push changes.

## 🌐 Supported Exchanges
The script fetches prices from:
- 🌐 **CoinPaprika** - `https://api.coinpaprika.com/`
- 💎 **CoinGecko** - `https://api.coingecko.com/`
- 🌐 **KuCoin** - `https://api.kucoin.com/`
- 💎 **Bitfinex** - `https://api-pub.bitfinex.com/`

## 📊 Example JSON Output
```json
{
    "BTC": [
        {
            "price": 43500.25,
            "source": "CoinPaprika",
            "timestamp": "2025-04-02 12:00:00 UTC"
        }
    ],
    "ETH": [
        {
            "price": 3050.75,
            "source": "CoinGecko",
            "timestamp": "2025-04-02 12:00:00 UTC"
        }
    ]
}
```

## 👨‍💻 Contributing
Pull requests are welcome! If you want to contribute:
1. **Fork** the repository
2. **Create a new branch** (`git checkout -b feature-branch`)
3. **Commit your changes** (`git commit -m "Added feature X"`)
4. **Push to the branch** (`git push origin feature-branch`)
5. **Create a pull request** ✅

## 📧 Contact
For questions or collaboration, contact **Mahkia Golbashi** at 📩 [mahkiagolbashi@gmail.com](mailto:mahkiagolbashi@gmail.com).

## 📚 License
This project is licensed under the **MIT License**. 📝

