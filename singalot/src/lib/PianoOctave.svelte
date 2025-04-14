<!-- svelte-ignore a11y_click_events_have_key_events -->
<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
<script lang="ts">
	// Import SVG assets
	import WhiteKeySvgRect from './keys/WhiteKeySvgRect.svelte';
	import BlackKeySvgRect from './keys/BlackKeySvgRect.svelte';
	import { blackSemitones, whiteSemitones, type BlackSemitone, type Semitone } from './names';

	type Props = {
		selectedSemitones: Semitone[];
		width?: number;
	};

	const { selectedSemitones, width = 200 }: Props = $props();
	const height = $derived(width * 0.63);

	const blackKeyPositions: Record<BlackSemitone, number> = {
		1: 14,
		3: 41,
		6: 82,
		8: 107,
		10: 133
	};

</script>

<div class="piano-octave" style="width: {width}px; height: {height}px;">
	<svg class="piano-octave-svg" xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 165 103">
		<!-- all white keys -->
		{#each whiteSemitones as key, i}
			<g transform="translate({i * 23},0)">
				<WhiteKeySvgRect selected={false} />
			</g>
		{/each}

		<!-- selected white keys on top -->
		{#each whiteSemitones as st, i}
			{#if selectedSemitones.includes(st)}
				<g transform="translate({i * 23},0)">
					<WhiteKeySvgRect selected={true} />
				</g>
			{/if}
		{/each}

		<!-- all black keys -->
		{#each blackSemitones as st}
			{@const position = blackKeyPositions[st]}
			<g transform="translate({position},0)">
				<BlackKeySvgRect selected={false} />
			</g>
		{/each}

		<!-- selected black keys on top -->
		{#each blackSemitones as st}
			{#if selectedSemitones.includes(st)}
				{@const position = blackKeyPositions[st]}
				<g transform="translate({position},0)">
					<BlackKeySvgRect selected={true} />
				</g>
			{/if}
		{/each}

	</svg>
</div>

<style>
	.piano-octave {
		position: relative;
	}

</style>
