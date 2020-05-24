---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: main
title: BW.dev | Blog
---
<ul class="py-2">
  {% for post in site.posts %}
    <li class="mb-6">
      <div class="flex flex-col items-start leading-relaxed">
      <a href="{{ post.url }}">
        <div class="mb-2 text-xl italic font-display text-copy-primary">{{ post.title }}</div>
      </a>
        <div class="self-end mb-3 text-xs text-copy-ternary font-display">Posted on: {{ post.date | date_to_string }}</div>
        <div class="text-sm leading-relaxed text-copy-secondary font-body">{{ post.excerpt }}</div>
      </div>
    </li>
  {% endfor %}
</ul>