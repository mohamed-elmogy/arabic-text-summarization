System Functionality
This Project is about automatic text summarization using deep learning for the Arabic language.
We present Al Zatona web interface that takes input as plain text, word doc, image, or voice, providing functionality and flexibility for the user.
We summarize text abstractivly or extractivly.
![image](https://github.com/mohamed-elmogy/arabic-text-summarization/assets/85038174/3574c5fc-4345-4a7a-803f-f6538fee1586)
Research
We have researched the best methods and techniques and performed a literature review and have decided that the best route to take was deep learning and have concluded to use transformers as they achieve SOTA performance.
We started by exploring the different methods that could be used to perform summarization, and hence the options that presented themselves to us were,
1.	Recurrent Neural Networks.
2.	Rhetorical Structure Theory. 
3.	Transformer-based solutions.

We chose to use transformers for a variety of reasons, of which is the beforehand established supremacy of the transformers over the other two options as detailed in the deep learning literature for the past six years.
The transformer is also very widely supported and used which facilities infrastructure and pretrained models.
Its GPU Friendly nature was also a contributing factor to our choice, due to the limitations on available hardware.
After that we were presented by choosing the sub tasks to work on, we choose the abstractive and extractive subtasks because they are the most broadly studied subtasks.
For the abstractive task, we were faced with the options of using the mT5 and mBART50, and as a result we performed a comparison between to find the best performing model, Fortunately, a previous paper, performed such a comparison and mBART+ a top, which is not open source, so we decided to use mBART50.
Then we found out that there exists an Arabic version of the BART model called the AraBART, which we are currently using.
For the extractive task, previous work utilised the AraBERT model, either through using it alone or alongside clustering.
And as logical extension to that work, we tried to do the same but with improved techniques, such as using better variants of AraBERT, such as AraELECTRA and Arabic ALBERT, and utilizing better clustering techniques.

However, doing so proved to be near impossible for a multitude of reasons.
1-	All Traditional techniques, not just clustering, are extremely difficult to implement with the Arabic languages, for examples, the very structure of the language is very unique and different from other languages, omitting the option of using methods that rely on the structural properties of the language.

Moreover, the expressive richness of the Arabic language is a large roadblock as well, due to the fact a word could have numerous synonyms, and a meaning could be described many words, making it very difficult to use cluster words using unsupervised and rule-based methods, not to mention the fact that the quality of the summary is very sensitive to the number of clusters.

Another issue is that lingual separators are rarely used in the Arabic language, which makes clustering a nightmare.
2-	All autoencoding models were unavailable to train on summarization, they were not implemented on hugging face for extractive summarization, the configuration of hugging face made it impractical for us to implement it ourselves (would have disrupted the entire workflow of the hugging face system and would have made debugging very messy).

Not to mention the fact all available models on GitHub were either already finetuned on other tasks or would have needed the aid of traditional methods. 
3-	The available data is simply not good enough, KALIMAT, the larger extractive data set is a generated, using it for training kept the model at square 0, figuratively and literary, when training on KALIMAT the produced rouge metrics were all zeros for all epochs.

As a last effort, we tried to fine tune the autoregressive models mT5 and AraBART on EASC and used 50 samples out of the 150 as a validation.

