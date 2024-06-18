library(shiny)
library(ggplot2)
library(tidyr)
library(plotly)

data <- read.csv('data/TPMs_table_100genes.csv')

function(input, output, session) {

    # update selectInput based on user's choice
    observe({
      updateSelectInput(session, 'genes', choices=data$GeneID)
    })
  
    output$gene_exp <- renderPlotly({
        x <- input$genes # get the selected gene
        selected_data <- data[data$GeneID == x, ] # get the whole row for selected GeneID
        
        # transform the row to its long version containing all six samples
        long <- selected_data %>%
          tidyr::pivot_longer(
          cols=matches('Control|Treated'), names_to='Sample', values_to='Expression'
        )
        
        # create a scatter plot using ggplot
        ggplot(long, aes(x=Sample, y=Expression, color=Sample)) +
          geom_point(size=5, shape=18) +
          theme_minimal() +
          ylim(0, max(long$Expression)) # start Y axis with 0 for the rendered plot
    })
}
