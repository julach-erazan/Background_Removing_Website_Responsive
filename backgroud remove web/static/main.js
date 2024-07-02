document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.getElementById("file");
  const previewSection = document.getElementById("preview-section");
  const previewImg = document.getElementById("preview-img");
  const removeBgBtn = document.getElementById("remove-bg-btn");
  const cancelBtn = document.getElementById("cancel-btn");

  fileInput.addEventListener("change", function (event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        previewImg.src = e.target.result;
        previewSection.style.display = "block";
      };
      reader.readAsDataURL(file);
    }
  });

  cancelBtn.addEventListener("click", function () {
    fileInput.value = "";
    previewImg.src = "#";
    previewSection.style.display = "none";
  });

  removeBgBtn.addEventListener("click", function () {
    // Logic to remove background
    alert("Background removed!"); // Replace with actual background removal logic
  });
});
