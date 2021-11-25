const textareaBtn = document.getElementById("btn-text");
const imgBtn = document.getElementById("btn-image");

const uploadDiv = document.getElementById("upload-div");
const textarea = document.getElementById("textarea");
const file = document.getElementById("file");
const img = document.getElementById("img");

textareaBtn.onclick = () => {
    asciipie('text')
};
imgBtn.onclick = () => {
    asciipie('img')
};

img.onload = () => {
    img.scrollIntoView({behavior: 'smooth'});
    textarea.style.display = "none";
}

file.onchange = () => {
    const file_to_upload = file.files[0];
    if (!file_to_upload) return;

    const uploadImg = document.createElement("img");
    uploadImg.src = URL.createObjectURL(file_to_upload);
    uploadDiv.replaceChildren(uploadImg);
    img.style.display = "none";
}

function asciipie(type) {
    const file_to_upload = file.files[0];
    if (!file_to_upload) return;

    const formData = new FormData();
    formData.append('file', file_to_upload);
    fetch('/upload?type=' + type, {
        method: 'POST',
        body: formData
    }).then(response => {
        if (type === 'img') {
            return response.blob();
        } else {
            img.style.display = "none";
            return response.text();
        }
    }).then(response => {
        if (type === 'img') {
            img.src = URL.createObjectURL(response);
            img.style.display = "inline";
        } else {
            textarea.textContent = response;
            textarea.style.display = "inline";
            textarea.style.height = (textarea.scrollHeight) + "px";
            textarea.scrollIntoView({behavior: 'smooth'});
        }
    });
}