#' This package help with discovering data properties, such as column names, their type and the number of missing values.
#'
#' @param data The name of the dataset.
#' @return Returns the variable names, type of columns and number of missing values in  \code{data}.
#' @examples
#' datadesc(gss)

datadesc <- function(data) {print(
  columns(data)
  sapply(data, class)
  sum(is.na(data$col)))
  }
datadesc("gss")

devtools::check()
devtools::document()

devtools::install_github()
