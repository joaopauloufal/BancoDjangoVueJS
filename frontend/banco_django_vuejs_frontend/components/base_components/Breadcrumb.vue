<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><nuxt-link to="/">Início</nuxt-link></li>
      <slot></slot>
    </ul>
  </nav>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

@Component
export default class Breadcrumb extends Vue {

}
</script>
