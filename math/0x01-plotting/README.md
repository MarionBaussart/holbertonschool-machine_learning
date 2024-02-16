# 0x01-plotting
## 0. Line Graph
Complete the source code to plot y as a line graph:
- y should be plotted as a solid red line
- The x-axis should range from 0 to 10
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/664b2543b48ef4918687.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221205%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221205T193829Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=40d5906d812c1af2ae299f1baaef9ef07568215c3822dbfaf86089a4b533be9f)

## 1. Scatter
Complete the source code to plot x ↦ y as a scatter plot:

- The x-axis should be labeled Height (in)
- The y-axis should be labeled Weight (lbs)
- The title should be Men's Height vs Weight
- The data should be plotted as magenta points
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/1b143961d254e65afa2c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221205%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221205T193829Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=14d5b81b224c4ca8473834b1eaeac60c90ce77c79624fcc410cf595bdaf2aa8d)

## 2. Change of scale
Complete the source code to plot x ↦ y as a line graph:

- The x-axis should be labeled Time (years)
- The y-axis should be labeled Fraction Remaining
- The title should be Exponential Decay of C-14
- The y-axis should be logarithmically scaled
- The x-axis should range from 0 to 28650
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/2b6334feb069ae1b6014.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221205%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221205T193829Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6970cfb21451c75747842ce305c1ef28480753f1858e302dcf5d17d154759036)

## 3. Two is better than one
Complete the source code to plot x ↦ y1 and x ↦ y2 as line graphs:

- The x-axis should be labeled Time (years)
- The y-axis should be labeled Fraction Remaining
- The title should be Exponential Decay of Radioactive Elements
- The x-axis should range from 0 to 20,000
- The y-axis should range from 0 to 1
- x ↦ y1 should be plotted with a dashed red line
- x ↦ y2 should be plotted with a solid green line
- A legend labeling x ↦ y1 as C-14 and x ↦ y2 as Ra-226 should be placed in the upper right hand corner of the plot
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/39eac4e8c8eb71469784.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221205%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221205T193830Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=acf071bf2c81c530e7ed24ef398fcbe26be8da930841fd0ddb5928e3ce98b142)

## 4. Frequency
Complete the source code to plot a histogram of student scores for a project:

- The x-axis should be labeled Grades
- The y-axis should be labeled Number of Students
- The x-axis should have bins every 10 units
- The title should be Project A
- The bars should be outlined in black
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/10a48ad296d16ee8fb63.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221205%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221205T193830Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8a9d92dc836286ca0e7b0a016d77da6c5cbe5e9af4b53c6d7223d9a1acfc1c3b)

## 5. All in One
Complete the source code to plot all 5 previous graphs in one figure:

- All axis labels and plot titles should have a font size of x-small (to fit nicely in one figure)
- The plots should make a 3 x 2 grid
- The last plot should take up two column widths (see below)
- The title of the figure should be All in One
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/e58d423ffd060a779753.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221205%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221205T193830Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=72dfb5a0128f1b3407a2be4edf23c64dee3b9375589fa1e06c3691e09d4e52ec)

## 6. Stacking Bars
Complete the source code to plot a stacked bar graph:

- fruit is a matrix representing the number of fruit various people possess
    - The columns of fruit represent the number of fruit Farrah, Fred, and Felicia have, respectively
    - The rows of fruit represent the number of apples, bananas, oranges, and peaches, respectively
- The bars should represent the number of fruit each person possesses:
    - The bars should be grouped by person, i.e, the horizontal axis should have one labeled tick per person
    - Each fruit should be represented by a specific color:
        - apples = red
        - bananas = yellow
        - oranges = orange (#ff8000)
        - peaches = peach (#ffe5b4)
        - A legend should be used to indicate which fruit is represented by each color
    - The bars should be stacked in the same order as the rows of fruit, from bottom to top
    - The bars should have a width of 0.5
- The y-axis should be labeled Quantity of Fruit
- The y-axis should range from 0 to 80 with ticks every 10 units
- The title should be Number of Fruit per Person
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/10/8058e8f96e697612d50d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221205%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221205T193830Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3289aaef7ff5e5db590825a96c1701bbcf1412c89d3595f3f5f8d0bf668ffe1f)

## 7. Gradient
Complete the source code to create a scatter plot of sampled elevations on a mountain:

- The x-axis should be labeled x coordinate (m)
- The y-axis should be labeled y coordinate (m)
- The title should be Mountain Elevation
- A colorbar should be used to display elevation
- The colorbar should be labeled elevation (m)
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/209d635d81bc43ca9ba5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221205%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221205T193830Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=aa4f2dd1fad48f145663b07baa95daf7dd147253d4265054e1f2f12c3d3c7e7b)

## 8. PCA
![Getting Started](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/9/a5834eeaf3eaa42c6530.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221205%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221205T193830Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a5e261ce8e77a1cb5fd7d40b9227dce8769f14c7bf0797ae1fc4b3848df16985)