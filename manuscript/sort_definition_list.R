sort_def_list <- function(in_file, out_file = NULL) {
  library(stringr)
  library(dplyr)
  
  data <- readLines(in_file)
  
  # Extract, remove yaml header
  yaml <- which(data == "---")
  head <- c(data[yaml[1]:yaml[2]], "\n")
  data <- data[(yaml[2]+1):length(data)]
  
  # Indexing lines
  def_start <- which(stringr::str_detect(data,  "^: ")) - 1
  def_end <- c(def_start[2:length(def_start)] - 1, length(data))
  
  def_ranges <- dplyr::data_frame(term = data[def_start],
                                  start = def_start,
                                  end = def_end) %>%
    dplyr::arrange(term) %>%
    dplyr::mutate(new_start = 
                    cumsum(
                      c(1, (end-start+1)[-length(term)])
                      )
                  ) %>%
    dplyr::mutate(new_end = new_start + (end-start))
  
  
  # Create ordered definition list
  data2 <- rep(NA, length(data))
  for (i in seq_along(def_ranges$term)) {
    start <- def_ranges$start[i]
    end <- def_ranges$end[i]
    n_start <- def_ranges$new_start[i]
    n_end <- def_ranges$new_end[i]
    data2[n_start:n_end] <- data[start:end]
  }
  
  # Rewrite rmd
  if (is.null(out_file)) out_file <- in_file
  data2 <- c(head, data2[!is.na(data2)])
  writeLines(paste(data2, collapse = "\n"),out_file)
}