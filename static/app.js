document.getElementById('askform').onsubmit = async(e) => {
    e.preventDefault();
    let formData = new FormData(e.target);

    let loading = document.getElementById("ans-loading");
    loading.style.display = "block"; //show loader

    let res = await fetch("/ask",{
        method: "POST",
        body: formData
    });

    let data = await res.json();
    document.getElementById("answer").innerText = data.answer;

    loading.style.display = "none"; //hide loader
};




document.getElementById('email-form').onsubmit = async(e) => {
    e.preventDefault();
    let formData = new FormData(e.target);

    let loading = document.getElementById("summary-loading");
    loading.style.display = "block"; //show loader

    let res = await fetch("/summarize",{
        method: "POST",
        body: formData
    });

    let data = await res.json();
    document.getElementById("summary").innerText = data.summary;

    loading.style.display = "none"; //hide loader
};