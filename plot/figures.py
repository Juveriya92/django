import matplotlib.pyplot as plt


def my_fig():
    fig,ax=plt.subplots()
    ax.plot([2,4,6,8],[3,5,7,9])
    return fig