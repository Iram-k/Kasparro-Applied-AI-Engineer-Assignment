# src/agents/data_agent.py
import pandas as pd
from .base import Agent

class DataAgent(Agent):
    def __init__(self, config: dict):
        super().__init__("DataAgent")
        self.config = config
        self.df = None

    def load_data(self):
        path = self.config["data"]["path"]
        df = pd.read_csv(path)
        df["date"] = pd.to_datetime(df["date"])
        if self.config["data"].get("use_sample", False):
            frac = self.config["data"].get("sample_frac", 0.3)
            df = df.sample(frac=frac, random_state=self.config["data"]["random_seed"])
        self.df = df
        return df

    def basic_summary(self):
        df = self.df
        return {
            "rows": len(df),
            "date_min": df["date"].min().strftime("%Y-%m-%d"),
            "date_max": df["date"].max().strftime("%Y-%m-%d"),
            "mean_roas": df["roas"].mean(),
            "mean_ctr": df["ctr"].mean(),
        }

    def roas_trend(self, freq="D"):
        df = self.df.copy()
        trend = (df
                 .groupby(pd.Grouper(key="date", freq=freq))["roas"]
                 .mean()
                 .reset_index())
        return trend

    def campaign_summary(self):
        df = self.df.copy()
        grouped = df.groupby("campaign_name").agg(
            spend=("spend", "sum"),
            impressions=("impressions", "sum"),
            clicks=("clicks", "sum"),
            purchases=("purchases", "sum"),
            revenue=("revenue", "sum"),
            avg_roas=("roas", "mean"),
            avg_ctr=("ctr", "mean")
        ).reset_index()
        grouped["cpc"] = grouped["spend"] / grouped["clicks"].clip(lower=1)
        grouped["cvr"] = grouped["purchases"] / grouped["clicks"].clip(lower=1)
        return grouped

    def low_ctr_segments(self, threshold: float):
        cs = self.campaign_summary()
        return cs[cs["avg_ctr"] < threshold].sort_values("avg_ctr")
