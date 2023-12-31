---
layout: default
author: Vincent Gramoli
title: Blog - Thinking Distributed 
description: This blog aims at being thought provoking and covers subjects related to the distributed nature of blockchain systems.
permalink: /blog/
author_profile: true
---

<h2>Latest Posts</h2>
<ul>
  {% for post in site.posts %}
    <li>
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>
