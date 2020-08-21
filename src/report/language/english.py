from textwrap import dedent
from typing import Any, Dict

from base.type import ConfigType
from report.base import BaseReportManager


class EnglishReportManager(BaseReportManager):
    def _formatted_header(self, config: ConfigType) -> str:
        return dedent(f"""
            # Welcome to {config["username"]}'s Contribution Report
            This report is auto generated by [contribution-markdown-report](https://github.com/lntuition/contribution-markdown-report).
            If you have any question or problem, please report [here](https://github.com/lntuition/contribution-markdown-report/issues).
            I hope this report will be a companion for your contribution trip :airplane:
        """)

    def _formatted_summary(self, config: ConfigType) -> str:
        return dedent(f"""
            ## Summary
            - **{config["today_date"]}** is **{config["total_length"]}th day** since the start of trip :sweat_smile:
            - There was **{config["today_cnt"] if config["today_cnt"] > 0 else "NO"}** new contribution 
            at **{config["today_date"]}**. {"Good job :+1:" if config["today_cnt"] > 0 else "Cheer up :muscle:"}
            - During the trip, total contribution count is **{config["total_cnt"]}** and average contribution count 
            is **{config["avg_cnt"]:.2f}**
            - Daily maximum contribution day is **{config["max_date"]}**, which is **{config["max_cnt"]}**.
            - Longest continous contribution trip was **{config["max_continous_length"]}** days 
            From **{config["max_continous_start_date"]}** to **{config["max_continous_end_date"]}** :walking:
            - Current continous contribution trip is **{config["cur_continous_length"]}** days 
            From **{config["cur_continous_start_date"]}** :running:
        """)

    def _config_graph(self) -> ConfigType:
        return {
            "section_name": "Graph",
            "count": {
                "x": "contribution",
                "y": "day",
                "title": {
                    "sum_recent": "Number of days per contribution up to the last 4 weeks",
                    "sum_full": "Number of days per contribution",
                },
            },
            "dayofweek": {
                "label": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                "x": "day of week",
                "y": "contribution",
                "title": {
                    "sum_recent": "Number of contribution per day of week up to the last 12 weeks",
                    "mean_full": "Average of contribution per day of week",
                },
            },
            "month": {
                "label": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "x": "month",
                "y": "contribution",
                "title": {
                    "sum_recent": "Number of contribution per month up to the last year",
                    "mean_full": "Average of contribution per month",
                },
            },
        }
