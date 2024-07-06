# Core library imports: Data visualization setup
import plotly.express as px
from streamlit import plotly_chart
from typing import List

def line_chart(title: str, labels: List[str], values: List[int], x_label: str, y_label: str) -> None:
    # Create a line chart using Plotly Express
    figure = px.line(
        title=title,
        x=labels,
        y=values,
        labels={'x': x_label, 'y': y_label},
        line_shape='linear'
    )
    plotly_chart(figure, use_container_width=True)

def area_chart(title: str, article_ids: List[str], percentages: List[float], x_label: str, y_label: str,
               sentiments: List[str], colors: List[str]) -> None:
    # Create an area chart using Plotly Express
    figure = px.area(
        title=title,
        x=article_ids,
        y=percentages,
        labels={'x': x_label, 'y': y_label},
        color=sentiments,
        color_discrete_sequence=colors
    )
    plotly_chart(figure, use_container_width=True)

def stacked_bar_chart(title: str, article_ids: List[str], percentages: List[float], x_label: str, y_label: str,
                      sentiments: List[str], colors: List[str]) -> None:
    # Create a stacked bar chart using Plotly Express
    figure = px.bar(
        title=title,
        x=article_ids,
        y=percentages,
        labels={'x': x_label, 'y': y_label},
        barmode='stack',
        color=sentiments,
        color_discrete_sequence=colors
    )
    plotly_chart(figure, use_container_width=True)

def pie_chart(title: str, labels: List[str], values: List[float], colors: List[str]) -> None:
    # Create a pie chart using Plotly Express
    figure = px.pie(
        title=title,
        names=labels,
        values=values,
        color_discrete_sequence=colors
    )
    plotly_chart(figure, use_container_width=True)

def horizontal_bar_chart(title: str, counts: List[int], labels: List[str], x_label: str, y_label: str, colors: List[str]) -> None:
    # Create a horizontal bar chart using Plotly Express
    figure = px.bar(
        title=title,
        x=counts,
        y=labels,
        labels={'x': x_label, 'y': y_label},
        orientation='h',
        text=counts,
        color=labels,
        color_discrete_sequence=colors
    )
    plotly_chart(figure, use_container_width=True)
