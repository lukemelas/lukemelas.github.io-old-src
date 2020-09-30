Title: Research
Date: 2020-10-01
Modified: 2020-10-01
Tags: about, luke, research, publications, melas, kyriazi, melas-kyriazi
Slug: research
Authors: Luke Melas-Kyriazi
Summary: Research

<!-- CSS Styles for Page -->
<style>
div.page-container.page-container {
    margin-top: 0px;
}
div.article-header-container.article-header-container {
    display: none;
}
</style>


<!-- CSS Styles for the project cards -->
<style>

    .projects-container {
        margin-bottom: 40px;
    }

    .project {
        background-color: #f7f7f7;
        border-radius: 10px;
        box-shadow: 0 0px 10px rgba(0, 0, 0, 0.05);
        display: flex;
        max-width: 100%;
        overflow: hidden;
        width: 100%;
        transition: box-shadow 0.2s ease-in-out;
    }

    .dark-theme .project {
        background-color: #2f3335;
    }
    
    .project:hover {
        box-shadow: 0 0px 10px rgba(0, 0, 0, 0.20);
    }

    .project.project h4 {
        letter-spacing: 1px;
        margin: 10px 0 5px 0;
        font-weight: bold;
        font-size: 16px;
        line-height: 1.4;
    }
    
    .project.project h5 {
        opacity: 0.6;
        margin: 0;
        letter-spacing: 1px;
        font-style: italic;
        font-size: 15px;
    }

    .project.project h6 {
        opacity: 0.8;
        margin: 0;
        letter-spacing: 1px;
        /* font-style: italic; */
        font-size: 15px;
    }

    .project-preview {
        /* color: #fff; */
        width: 33%;
        max-width: 250px;
        background-color: #2A265F;
        background-size: cover;
        background-position: center;
        padding: 0px;
        opacity: 60%;
        transition: opacity 0.4s ease-in-out;
    }

    .project:hover .project-preview {
        opacity: 80%;
    }

    .project-info {
        padding: 10px 30px;
        position: relative;
        width: 100%;
    }

    .btn {
        background-color: #2A265F;
        border: 0;
        border-radius: 50px;
        color: #fff;
        padding: 12px 25px;
        position: absolute;
        bottom: 30px;
        right: 30px;
        letter-spacing: 1px;
    }

    .project-links {
        margin-top: 10px;
    }

    .project-links.project-links a {
        padding: 0px 40px 0px 0px;
        text-decoration: none;
        font-size: 14px;
        color: #2a265f;
    }

    .project-info p {
        font-size: 14px;
    }

    @media only screen and (max-width: 600px) {
        .project-preview {
            display: none;
        }
    }



</style>

#### Publications 

<!-- TEMPLATE -->
<!-- <div class="projects-container">
	<div class="project">
		<div class="project-preview" 
             style="background-image: url('/assets/images/research/[FILENAME]')">
        </div>
		<div class="project-info">
			<h4>Title</h4>
			<h5>Authors</h5>
			<h6>Venue</h6>
            <div class="project-links">
                <a href="#">Paper</a>
                <a href="#">Project Page</a>
                <a href="#">GitHub</a>
            </div>
		</div>
	</div>
</div> -->


<div class="projects-container">
	<div class="project">
		<div class="project-preview" 
             style="background-image: url('/assets/images/research/show-edit-tell.png')">
        </div>
		<div class="project-info">
			<h4>Show, Edit and Tell: A Framework for Editing Image Captions</h4>
			<h5>Fawaz Sammani, Luke Melas-Kyriazi</h5>
			<h6>CVPR 2020</h6>
            <div class="project-links">
                <a href="https://arxiv.org/abs/2003.03107">Paper</a>
                <a href="https://github.com/fawazsammani/show-edit-tell">GitHub</a>
            </div>
		</div>
	</div>
</div>


<div class="projects-container">
	<div class="project">
		<div class="project-preview" 
             style="background-image: url('/assets/images/research/aging-cover.png')">
        </div>
		<div class="project-info">
			<h4>Prediction of Chronological and Biological Age from Laboratory Data</h4>
			<h5>Luke Sagers, Luke Melas-Kyriazi, Chirag Patel, Arjun Manrai</h5>
			<h6>Aging (Cover Article)</h6>
            <div class="project-links">
                <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7244024/">Paper</a>
            </div>
		</div>
	</div>
</div>

<div class="projects-container">
	<div class="project">
		<div class="project-preview" 
             style="background-image: url('/assets/images/research/generation-distillation.png')">
        </div>
		<div class="project-info">
			<h4>Generation-Distillation for Efficient NLU in Low-Data Settings</h4>
			<h5>Luke Melas-Kyriazi, George Han, Celine Liang</h5>
			<h6>EMNLP 2019 Workshop on Low-resource NLP</h6>
            <div class="project-links">
                <a href="https://arxiv.org/abs/2002.00733">Paper</a>
            </div>
		</div>
	</div>
</div>

<div class="projects-container">
	<div class="project">
		<div class="project-preview" 
             style="background-image: url('/assets/images/research/ea-adaptation.png')">
        </div>
		<div class="project-info">
			<h4>Encoder-agnostic Adaptation for Conditional Language Generation</h4>
			<h5>Zachary Ziegler, Luke Melas-Kyriazi, Sebastian Gehrmann, Alexander Rush</h5>
			<!-- <h6>:'(</h6> -->
            <div class="project-links">
                <a href="https://arxiv.org/abs/1908.06938">Paper</a>
                <a href="https://github.com/harvardnlp/encoder-agnostic-adaptation">GitHub</a>
            </div>
		</div>
	</div>
</div>

<div class="projects-container">
	<div class="project">
		<div class="project-preview" 
             style="background-image: url('/assets/images/research/image-paragraph-captioning.png')">
        </div>
		<div class="project-info">
			<h4>Training for Diversity in Image Paragraph Captioning</h4>
			<h5>Luke Melas-Kyriazi, Alexander Rush, George Han</h5>
			<h6>EMNLP 2018</h6>
            <div class="project-links">
                <a href="https://www.aclweb.org/anthology/D18-1084/">Paper</a>
                <a href="https://github.com/lukemelas/image-paragraph-captioning">GitHub</a>
            </div>
		</div>
	</div>
</div>

#### Projects

<div class="projects-container">
	<div class="project">
		<div class="project-preview" style="background-image: url('/assets/images/research/efficientnet.png')">
		</div>
		<div class="project-info">
			<h4>EfficientNet-PyTorch</h4>
			<p>A fast and easy-to-use implementation of <a href="https://arxiv.org/abs/1905.11946">EfficientNet</a> in PyTorch <br />(5000 GitHub stars).</p>
            <div class="project-links">
                <a href="https://github.com/lukemelas/EfficientNet-PyTorch">GitHub</a>
            </div>
		</div>
	</div>
</div>

<div class="projects-container">
	<div class="project">
		<div class="project-preview" style="background-image: url('/assets/images/colorization/model.jpg')">
		</div>
		<div class="project-info">
			<h4>Image Colorization</h4>
			<p>Image colorization using deep convolutional neural networks, originally started as a class project. </p>
            <div class="project-links">
                <a href="https://github.com/lukemelas/Automatic-Image-Colorization">GitHub</a>
            </div>
		</div>
	</div>
</div>









