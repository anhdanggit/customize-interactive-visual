# CUSTOMIZING VISUALIATION IN PYTHON
---
This is a part of my trainings in the **Coursera Specilization in Applied Data Science** by the Univerisity of Michigan.
Due to the variety of tasks in real-life worlds, frequently the basic plots and templates are not enough. 
In these examples, I will touch further to the very first layers of backend of Python, to modify the graphs for the more efficient illustration. 

## Weather Plot
It is a nice example about cleaning data, designing the graphs. The graphs contains different variables, with the high-record and low-record temperature. The space between them is shaded. The scatters present the record-broken temperature in 2015. There are also modification the axes components for better visualization. 
![alt text](https://github.com/maianhdang/customize_visual/blob/master/results/weather_plot.png)

The plot is tried to follow the below criteria:
* TRUTHFUL: I try to make the visual clear in information, by transforming the x-axis labels into readable and natural format (more details in the source code)

* INSIGHTFUL: Similar to the y-axis label, I add the minor ticks to the graph, so it separates the first half and the second half of each month. Hopefully, it will be more informative about the seasonal transition of the weather. 

* BEAUTY: I modify the transparency to make the lines and shading lighter to look at, also reduce the ink-ratio. Also, I choose the size of scattering points not too big (then they will not be crowded and hide other details), but not too small to see. I choose the colors easy for the eyes (not too colorful)

* FUNCTIONALITY: The legend is added to ensure every detail of the visual is well-explained. Unnecessary details (such as box, title of the legend, y-axis title are removed) to reduce the ink-ratio. I also try to minimize the details of the visual (grids, background, unnecessary/duplicated info)

## Interactive and Animations
I make an more advanced visualization: 
* Bar coloring folows the scale: dark blue for the distribution being certainly below this y-axis, to white if the value is certainly contained, to dark red if the value is certainly not contained
* Users can interactively choose the y-axis reference line
* As a bonus, I made an animation for the changes of reference line
![alt text](https://github.com/maianhdang/customize_visual/blob/master/results/interactive.png)
