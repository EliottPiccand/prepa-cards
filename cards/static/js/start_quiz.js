window.addEventListener("load", (event) => {
    document.querySelectorAll("[show-div]").forEach((element) => {
        const divId = element.getAttribute("show-div")
        const div = document.getElementById(divId)

        if (element.checked) {
            div.classList.remove("hidden")
        } else {
            div.classList.add("hidden")
        }

        element.addEventListener("change", (event) => {
            if (element.checked) {
                div.classList.remove("hidden")
            } else {
                div.classList.add("hidden")
            }
        })
    })

    document.querySelectorAll("[show-attr]").forEach((element) => {
        const attrName = element.getAttribute("show-attr")
        document.querySelectorAll(`[${attrName}]`).forEach(el => {
            if (element.checked) {
                el.classList.remove("hidden")
            } else {
                el.classList.add("hidden")
            }
    
            element.addEventListener("change", (event) => {
                if (element.checked) {
                    el.classList.remove("hidden")
                } else {
                    el.classList.add("hidden")
                }
            })
        })
    })

    document.querySelectorAll("[unselect-all]").forEach((element) => {
        element.addEventListener("click", (event) => {
            const divId = element.getAttribute("unselect-all")
            const div = document.getElementById(divId)
            div.querySelectorAll("[type='checkbox']").forEach((el) => {
                el.checked = false
            })
        })
    })
})