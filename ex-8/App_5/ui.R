library(shiny)
library(plotly)

data <- read.csv('data/TPMs_table_100genes.csv')

fluidPage(
    titlePanel("Gene expression"),
    sidebarLayout(
        sidebarPanel(
            selectInput('genes', 'Select a gene:', choices=data$GeneID)
        ),
        mainPanel(plotlyOutput("gene_exp"))
    )
)
