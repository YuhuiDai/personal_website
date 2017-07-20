var margin = {top: 10, right: 10, bottom: 10, left: 10},
                width = window.innerWidth*0.8;

            var formatNumber = d3.format(",.0f"),    // zero decimal places
                format = function(d) { return formatNumber(d) ; };

            // append the svg_sankey canvas to the page
            var svg_sankey = d3.select("#sankeyChart").append("svg")
                .attr("width", width)
                .attr("height", 250)
                .append("g");
//                .attr("transform",
//                    "translate(" + margin.left + "," + margin.top + ")");

            // Set the sankey diagram properties
            var sankey = d3.sankey()
                .nodeWidth(40)
                .nodePadding(5)
                .size([window.innerWidth -50, 250 ]);

            var path = sankey.link();

            // load the data
            d3.json("../sankey-formatted.json", function(error, graph) {
                sankey
                    .nodes(graph.nodes)
                    .links(graph.links)
                    .layout(32);

                var gradientLink = svg_sankey.append("g").selectAll(".gradient-link")
                    .data(graph.links)
                    .enter().append("path")
                    .attr("class", "gradient-link")
                    .attr("d", path)
                    .style("stroke-width", function(d) {
                        return Math.max(1, d.dy);
                    })
                    .sort(function(a, b) {
                        return b.dy - a.dy;
                    })
                    .style('stroke', function(d) {
                        var sourceColor = d.source.c;
                        var targetColor = d.target.c;
                        var id = 'c-' + sourceColor + '-to-' + targetColor;

                        var gradient = svg_sankey.append('defs')
                            .append('linearGradient')
                            .attr('id', id)
                            .attr('x1', '0%')
                            .attr('y1', '0%')
                            .attr('x2', '100%')
                            .attr('y2', '0%')
                            .attr('spreadMethod', 'pad');

                        gradient.append('stop')
                            .attr('offset', '0%')
                            .attr('stop-color', sourceColor);

                        gradient.append('stop')
                            .attr('offset', '100%')
                            .attr('stop-color', targetColor);

                        return "url(#" + id + ")";
                    });

                var link = svg_sankey.append("g").selectAll(".link")
                    .data(graph.links)
                    .enter().append("path")
                    .attr("class", "link")
                    .attr("d", path)
                    .style("stroke-width", function(d) { return Math.max(1, d.dy); });

                // add in the nodes
                var node = svg_sankey.append("g").selectAll(".node")
                    .data(graph.nodes)
                    .enter().append("g")
                    .attr("class", "node")
                    .attr("transform", function(d) {return "translate(" + d.x + "," + d.y + ")"; });

                node.append("text")
                    .attr("x", -6)
                    .attr("y", function(d) { return d.dy / 2; })
                    .attr("dy", ".35em")
                    .attr("text-anchor", "end")
                    .attr("transform", null)
                    .text(function(d) { return d.name; })
                    .filter(function(d) { return d.x < width / 2; })
                    .attr("x", 6 + sankey.nodeWidth())
                    .attr("text-anchor", "start");

                node.append("rect")
                    .attr("height", function(d) { return d.dy; })
                    .attr("width", sankey.nodeWidth())
                    .style("fill", function(d) {return d.color = d.c; })
                    .text(function(d) {return d.name; });

                function highlightConnected(g) {

                    gradientLink.filter(function (d) { return d.source === g || d.target === g; })
                      .style("stroke-opacity", 0.9);

                }

                function fadeUnconnected(g) {
                    
                    var relatedNames = [g.name];
                    
                    if (g.sourceLinks.length > 0) {
                        for (var i = 0; i< g.sourceLinks.length; i++) {
                            relatedNames.push(g.sourceLinks[i].target.name);
                        }
                    }
                    if (g.targetLinks.length > 0) {
                        for (var i = 0; i< g.targetLinks.length; i++) {
                            relatedNames.push(g.targetLinks[i].source.name);
                        }
                    }
                    
                    gradientLink.filter(function (d) {return d.source !== g && d.target !== g; })
                                .transition().duration(400).style("stroke-opacity", 0.1);

                    node.filter(function (d) { return !relatedNames.includes(d.name);})
                        .transition().duration(400).style("opacity", 0.1);
                  }

                function restoreLinksAndNodes() {

                    gradientLink.transition().duration(400).style("stroke-opacity", 0.7);
                    node.transition().duration(400).style('opacity', 1);    
                  }

                node.on("mouseenter", function (g) {
                    
                      restoreLinksAndNodes();
                      highlightConnected(g);
                      fadeUnconnected(g);
                    
                  });

                node.on("mouseleave", function () {
                      restoreLinksAndNodes();
                    
                  });


            });