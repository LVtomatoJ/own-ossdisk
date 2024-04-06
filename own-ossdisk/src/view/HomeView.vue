<template>
    index
</template>

<script setup>
import { useMyFetch } from '../request/useMyFetch';

const { isFetching, error, data } = useMyFetch('')

</script>