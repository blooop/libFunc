import matplotlib.pyplot as plt


def scaleBar(originX, originY, xScale=20, yScale=0.5, color="k"):
    xData = [originX - xScale, originX, originX]
    yData = [originY, originY, originY + yScale]
    plt.plot(xData, yData, color, linewidth=1)
    # plt.text(originX - xScale / 2, originY - 0.05, "20 ms", va='top', ha='center', color=color, fontsize=10) #scale bar length
    # plt.text(originX, originY + yScale / 2, " 0.5 mV", va='center', color=color, fontsize=10) #scale bar height


def quit_figure(event):
    print event.key
    if event.key == 'esc':
        plt.close(event.canvas.figure)


def plotErrorArea(times, means, errors, col, alphaVal=0.45):
    plt.errorbar(times, means, errors, linestyle="None", marker='.', linewidth=1, capsize=3, color=col)


def drawLabel(ax, text, xStart, xEnd, yCenter, height=1.5, color="Black"):
    xCenter = (xStart + xEnd) / 2
    xWidth = abs(xEnd - xStart)
    ax.add_patch(Rectangle((xStart, yCenter), xWidth, height, fill="True", alpha=1, facecolor=color))
    plt.text(xCenter, yCenter + height + 2, text, ha='center', color=color)
