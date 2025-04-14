<script lang="ts">
	import type { Mood } from "./names";

	type Props = {
		mood: Mood;
		hidden?: boolean;
		size?: number;
		onClick?: () => void;
	};
	const { mood, size = 80, hidden = false, onClick = () => {alert('1')} }: Props = $props();
</script>

<div class="emoji-container" style="font-size: {size}px;">
	<button onclick={onClick}>
		{#if hidden}
			🎶
		{:else if mood === 'happy'}
			<!-- Visible emoji for the game -->
			😊
		{:else if mood === 'sad'}
			😩
		{/if}
	</button>
</div>

<style>
	.emoji-container {
		user-select: none;
	}

	button {
		background: none;
		border: none;
		cursor: pointer;
	}
</style>
