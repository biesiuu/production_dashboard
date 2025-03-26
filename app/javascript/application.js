import "@hotwired/turbo-rails"
import "controllers"


document.addEventListener("turbo:load", () => {
  document.addEventListener("click", (e) => {
    const link = e.target.closest("a[data-turbo-method]")
    if (!link) return

    e.preventDefault()
    const method = link.dataset.turboMethod
    const url = link.href
    const confirmMsg = link.dataset.confirm

    if (confirmMsg && !window.confirm(confirmMsg)) return

    fetch(url, {
      method: method,
      headers: {
        "X-CSRF-Token": document.querySelector("[name='csrf-token']").content,
        "Accept": "text/html",
      },
    }).then(response => {
      if (response.redirected) {
        window.location.href = response.url
      }
    })
  })
})