window.addEventListener("load", (event) => {
    const questionDiv = document.getElementById("question")
    const answerDiv = document.getElementById("answer")

    answerDiv.classList.add("hidden")

    questionDiv.querySelector("a").addEventListener("click", (event) => {
        answerDiv.classList.remove("hidden")
        questionDiv.classList.add("hidden")
    })

    // Latex
    const toCompile = document.querySelectorAll(".latex-compile")
    toCompile.forEach((element) => {
        var generator = new latexjs.HtmlGenerator({ hyphenate: false })
        try {
            generator = latexjs.parse(element.textContent, { generator: generator })
            element.textContent = ""
            element.appendChild(generator.domFragment())
            var toRemove = document.querySelectorAll(".katex-html")
            if (toRemove) {
                toRemove.forEach((element) => {
                    element.remove()
                })
            }

            var toRemoveTwo = document.querySelectorAll(".mord.mathnormal")
            if (toRemoveTwo) {
                toRemoveTwo.forEach((element) => {
                    element.remove()
                })
            }
        } catch (error) {
            var p = document.createElement("p")
            p.classList.add(["text-sm"])
            p.classList.add(["text-red-400"])
            p.textContent = "Erreur de syntaxe"
            element.appendChild(p)
        }
    })
})