window.addEventListener("load", (event) => {
    const chapterSelect = document.getElementById("chapter")

    const yearSelect = document.getElementById("year")
    const subjectSelect = document.getElementById("subject")

    function updateChapter() {
        chapterSelect.querySelectorAll("option").forEach((element) => {
            if ((element.getAttribute("year") == yearSelect.value)
             && (element.getAttribute("subject-id") == subjectSelect.value)) {
                element.classList.remove("hidden")
            } else {
                element.classList.add("hidden")
            }
        })
    }

    yearSelect.addEventListener("change", (event) => {
        updateChapter()
    })

    subjectSelect.addEventListener("change", (event) => {
        updateChapter()
    })

    updateChapter()

    // Latex
    function setupLatexPlayground(id) {
        const textarea = document.getElementById(id)
        textarea.addEventListener("change", (event) => {
            var generator = new latexjs.HtmlGenerator({ hyphenate: false })
            const latexParentId = textarea.getAttribute("latex-parent")
            const latexParent = document.getElementById(latexParentId)
            Array.from(latexParent.children).forEach((el) => {
                el.remove()
            })

            try {
                generator = latexjs.parse(textarea.value, { generator: generator })

                latexParent.appendChild(generator.domFragment())
                var toRemove = document.querySelector(".katex-html")
                if (toRemove) {
                    toRemove.remove()
                }
            } catch (error) {
                var p = document.createElement("p")
                p.classList.add(["text-sm"])
                p.classList.add(["text-red-400"])
                p.textContent = "Erreur de syntaxe"
                latexParent.appendChild(p)
            }
        })
    }

    setupLatexPlayground("question")
    setupLatexPlayground("answer")
})