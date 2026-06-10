import plotly.graph_objects as go

def apply_theme(fig):

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#151C32",
        plot_bgcolor="#151C32",
        font_color="white",
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    return fig