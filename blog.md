---
layout: default
author: Vincent Gramoli
title: Blog - Thinking Distributed 
description: This blog aims at being thought provoking and covers subjects related to the distributed nature of blockchain systems.
permalink: /blog/
author_profile: false
---
<h1>Latest Posts</h1>

<ul>
  {% for post in site.posts %}
    <li>
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      {{ post.excerpt }}&nbsp;-&nbsp;{{ post.tags }}
    </li>
  {% endfor %}
</ul>
