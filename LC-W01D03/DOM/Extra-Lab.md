# 🧪 Lab: Interactive Comment Board

## 🎯 Goal

By the end of this lab, students will:

- Navigate and manipulate the DOM.
- Dynamically create and style elements.
- Use event listeners and delegation.
- Manage attributes and classes programmatically.

---

## ⏰ Time: 30–60 minutes

### Part 1: Setup

1. Open the provided **Replit template** (HTML/CSS/JS Static).
2. Replace everything inside `<body>...</body>` in `index.html` with this starter HTML:

```html
<h1 id="main-title">Comment Board</h1>
<p class="cool">Share your thoughts below 👇</p>

<input id="comment-input" placeholder="Type a comment..." />
<button id="add-comment-btn">Add Comment</button>

<ul id="comments">
  <li>First comment!</li>
</ul>

<img id="random-img" />
<a id="google-link">Visit Google</a>
```

---

## Part 2: Tasks

### 1. Selecting & Inspecting Elements

Use `getElementById` and `querySelector` to select:

- `#main-title`
- `.cool` paragraph
- `#comments` list

Log them with `console.dir()`.

---

### 2. Changing Content & Styles

- Change the `<p>` text to:  
  `"Welcome! Add as many comments as you like."`

- Use `style` to:
  - Center the `<h1>` text.
  - Make the `<p>` text **blue**.

---

### 3. Working with Attributes

- Select the `<img>` by ID.
- Set its `src` to a random placeholder image (use `https://picsum.photos/300`).
- Set its `alt` attribute to `"Random placeholder image"`.
- Select the `<a>` tag and programmatically set its `href` to `https://www.google.com`.

---

### 4. Adding Event Listeners

- Select the **Add Comment** button.
- Add a `click` listener that:
  - Creates a new `<li>` with the text from the input.
  - Appends it to the `<ul id="comments">`.
  - Clears the input after submission.

---

### 5. Event Delegation

- Add an event listener on the `<ul>` so that when any comment `<li>` is clicked:
  - The clicked text color changes to **red**.
  - Log the clicked element using `evt.target`.

---

### 6. Removing Event Listeners (Bonus)

- Write a named callback function for the button click (`handleAddComment`).
- Allow the event listener to be removed after 5 comments have been added.

---

## ❓ Review Questions

1. Which DOM method selects all elements matching a CSS selector?
2. What does `evt.target` represent?
3. Why is event delegation more efficient than attaching multiple event listeners?

---

## 🔥 Advanced Section (Extra: 60–75 min)

### Build a Mini To-Do List App

Extend your Comment Board into a To-Do list with full interactivity:

#### 1. Add Priority Styling

- When adding a comment, also add a `<select>` dropdown (`Low`, `Medium`, `High`).
- Apply different text colors depending on priority:
  - Green = low
  - Orange = medium
  - Red = high

#### 2. Add Delete Buttons

- Each `<li>` should have a small `"❌"` button.
- Clicking it removes only that comment.
- Use **event delegation** to handle all deletes.

#### 3. Toggle Completion

- Clicking the `<li>` text (not the delete button) toggles a CSS class `.done` that applies a **strikethrough style**.

#### 4. Clear All

- Add a new button `"Clear All"` that removes all `<li>` items at once.

#### 5. Extra Attribute Practice

- Store a **timestamp** in a custom `data-time` attribute for each new comment.
- Log it when the item is clicked.

---

## 📝 Deliverables

- A working interactive web page hosted in Replit.
- Students should be able to demonstrate:
  - DOM element selection and manipulation.
  - Event-driven interactivity.
  - Event delegation efficiency.
  - Attribute/class management in JS.
