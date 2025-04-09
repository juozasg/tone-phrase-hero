<script lang="ts">
	type Props = {
		mood: 'happy' | 'sad';
		size?: number;
	};
	const { mood, size = 80 }: Props = $props();
</script>

<div class="emoji-container" style="font-size: {size}px;">
	{#if mood === 'happy'}
		😊
	{:else if mood === 'sad'}
		😩
	{/if}
</div>

<style>
	.emoji-container {
		user-select: none;
	}
</style>
