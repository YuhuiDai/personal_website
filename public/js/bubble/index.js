$(document).ready(function () {
  var bubbleChart = new d3.svg.BubbleChart({
    supportResponsive: true,
    //container: => use @default
    size: 600,
    //viewBoxSize: => use @default
    innerRadius: 600 / 3.5,
    //outerRadius: => use @default
    radiusMin: 50,
    //radiusMax: use @default
    //intersectDelta: use @default
    //intersectInc: use @default
    //circleColor: use @default
    data: {
      items: [
        {text: "Java", category: "4", description: ""},
        {text: "Illustrator", category: "3", description: ""},
        {text: "Photoshop", category: "3", description: ""},
        {text: "Css", category: "2", description: ""},
        {text: "Html", category: "2", description: ""},
        {text: "Python", category: "4", description: ""},
        {text: "InDesign", category: "3", description: ""},
        {text: "Stata", category: "1", description: ""},
        {text: "R", category: "1", description: ""},
        {text: "Javascript", category: "4", description: ""}
      ],
      eval: function (item) {return item.category;},
      classed: function (item) {return item.text.split(" ").join("");}
    },
    plugins: [
      // {
      //   name: "central-click",
      //   options: {
      //     text: "there is more",
      //     style: {
      //       "font-size": "12px",
      //       "font-style": "italic",
      //       "font-family": "Source Sans Pro, sans-serif",
      //       //"font-weight": "700",
      //       "text-anchor": "middle",
      //       "fill": "white"
      //     },
      //     attr: {dy: "65px"},
      //     centralClick: function() {
      //       alert("Here is more details!!");
      //     }
      //   }
      // },
      {
        name: "lines",
        options: {
          format: [
            {// Line #0
              textField: "text",
              classed: {text: true},
              style: {
                "font-size": "20px",
                "font-family": "Source Sans Pro, sans-serif",
                "text-anchor": "middle",
                fill: "white"
              },
              attr: {
                dy: "0px",
                x: function (d) {return d.cx;},
                y: function (d) {return d.cy;}
              }
            }
            // {// Line #1
            //   textField: "description",
            //   classed: {description: true},
            //   style: {
            //     "font-size": "14px",
            //     "font-family": "Source Sans Pro, sans-serif",
            //     "text-anchor": "middle",
            //     fill: "white"
            //   },
            //   attr: {
            //     dy: "20px",
            //     x: function (d) {return d.cx;},
            //     y: function (d) {return d.cy;}
            //   }
            // }
          ],
          centralFormat: [
            {// Line #0
              style: {"font-size": "50px"},
              attr: {}
            },
            {// Line #1
              style: {"font-size": "30px"},
              attr: {dy: "40px"}
            }
          ]
        }
      }]
  });
});