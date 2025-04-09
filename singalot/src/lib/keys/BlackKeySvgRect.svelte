<script lang="ts">
	const { selected = false } = $props();

	const strokeWidth = $derived.by(() => {
		return selected ? 2 : 0;
	});

	const fill = $derived.by(() => {
		return selected ? '#808000' : '#000000';
	});

	const stroke = $derived.by(() => {
		return selected ? '#ffff33' : '#000000';
	});

	// const width = $derived.by(() => {
	// 	return selected ? 20 : 23;
	// });


</script>

<rect
	style="fill:{fill};stroke:{stroke};stroke-width:{strokeWidth}"
	width={selected ? 11 : 15}
	height={selected ? 60 : 64}
	x={selected ? 2 : 0}
	y={selected ? 0 : -2}
/>