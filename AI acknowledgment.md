# Reflection on the Use of Artificial Intelligence

## 1. Purpose of AI Use

Artificial intelligence (AI), specifically ChatGPT, was used as a supporting tool throughout the development of this project. Its primary purpose was to assist with understanding the project requirements, developing the Python workflow, interpreting numerical results, and documenting the work. The project investigates linear interpolation and cubic spline interpolation for reconstructing missing building temperature measurements.

## 2. Tasks Supported by AI

AI assistance was used during data preparation to understand the structure of the original dataset, identify duplicate timestamps, and select a suitable sensor for analysis. It also helped with the implementation and explanation of the interpolation methods, the calculation of mean absolute error (MAE) and root mean square error (RMSE), and the development of graphs comparing their performance.

Further assistance was used to prepare basic automated tests,and generate HTML source-code documentation. AI also provided guidance on organising the project files and preparing the GitHub repository.

## 3. Verification of AI-Assisted Work

An important part of the process was checking the outputs rather than accepting AI-generated suggestions without verification. The Python scripts were executed to confirm that the data could be processed and that the interpolation experiments produced numerical results. The automated test suite was also run, with all four tests passing.

The resulting MAE and RMSE values were compared between the two methods, and the graphs were inspected to ensure that they represented the calculated results. These checks provided evidence that the implemented calculations and selected workflow were operating as expected, although they do not establish that every part of the project is error-free.

## 4. Limitations and Critical Evaluation

The results highlighted the importance of critically evaluating AI-assisted analysis. The comparison showed that linear interpolation performed better than cubic spline interpolation for all three tested gap sizes. Rather than assuming that the more complex method must be more accurate, the conclusion was based on the calculated error metrics.

The investigation also identified limitations associated with varying measurement intervals, the use of recorded sensor values as reference values, and the difficulty of estimating temperatures across longer missing intervals. These limitations affect how confidently the results can be applied to real building-monitoring systems.

The four automated tests cover basic numerical operations rather than the entire project pipeline. Therefore, passing these tests does not guarantee that every script, data-processing step, or result is error-free.

## 5. Learning and Reflection

Using AI helped me progress through unfamiliar Python tasks and understand how a numerical investigation could be organised into data preparation, modelling, validation, comparison, and documentation. However, AI assistance also required me to check commands, understand the meaning of the outputs, and distinguish between successful execution and comprehensive validation.

The project reinforced the importance of reproducibility, numerical validation, and critically assessing computational results before using them to support engineering decisions. AI was most useful as a programming and learning assistant rather than as a substitute for engineering judgement.

## 6. Conclusion

AI supported several stages of this project, from data preparation and numerical implementation to testing and documentation. Its suggestions were evaluated against the code outputs, error metrics, graphs, and basic automated tests. The final engineering conclusions must remain supported by the actual experiments and their limitations.

The experience demonstrated that AI can help make technical work more manageable, but responsibility for understanding the methods, checking the results, acknowledging limitations, and presenting accurate conclusions remains with the student.