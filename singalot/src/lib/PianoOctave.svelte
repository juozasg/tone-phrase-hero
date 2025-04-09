<!-- svelte-ignore a11y_click_events_have_key_events -->
<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
<script lang="ts">
	// Import SVG assets
	import WhiteKeys from '$lib/assets/white-keys.svg';
	import WhiteKeySelected from '$lib/assets/white-key-selected.svg';
	import BlackKeys from '$lib/assets/black-keys.svg';
	import BlackKeySelected from '$lib/assets/black-key-selected.svg';
	import WhiteKeySvgRect from './keys/WhiteKeySvgRect.svelte';
	import BlackKeySvgRect from './keys/BlackKeySvgRect.svelte';

	type Props = {
		selectedKeys: string[];
		width?: number;
	};

	const { selectedKeys, width = 200 }: Props = $props();
	const height = $derived(width * 0.63);

	// Define white and black keys
	const whiteKeys = ['C', 'D', 'E', 'F', 'G', 'A', 'B'];
	const blackKeys = ['C#', 'D#', 'F#', 'G#', 'A#'];

	const blackKeyPositions: Record<string, number> = {
		'C#': 14,
		'D#': 41,
		'F#': 82,
		'G#': 107,
		'A#': 133
	};

	const selectedBlackPositions = $derived.by(() => {
		return selectedKeys
			.filter((key) => blackKeys.includes(key))
			.map((key) => blackKeyPositions[key]);
	});

	// $effect(() => {
	// 	console.log('Selected keys:', selectedKeys);
	// 	console.log('Selected black key positions:', selectedBlackPositions);
	// });
</script>

<div class="piano-octave" style="width: {width}px; height: {height}px;">
	<svg class="piano-octave-svg" xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 165 103">
		{#each whiteKeys as key, i}
			<g transform="translate({i * 23},0)">
				<WhiteKeySvgRect selected={false} />
			</g>
		{/each}

		{#each whiteKeys as key, i}
			{#if selectedKeys.includes(key)}
				<g transform="translate({i * 23},0)">
					<WhiteKeySvgRect selected={true} />
				</g>
			{/if}
		{/each}


		<!-- Render all black keys -->
		{#each Object.entries(blackKeyPositions) as [key, position], i}
			<g transform="translate({position},0)">
				<BlackKeySvgRect selected={false} />
			</g>
		{/each}

		{#each Object.entries(blackKeyPositions) as [key, position], i}
			{#if selectedKeys.includes(key)}
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
		/* background-color: aliceblue; */
	}

	/*
  .white-key-selected, .black-key-selected {
    position: absolute;
    top: 0;
    cursor: pointer;
  } */
</style>
