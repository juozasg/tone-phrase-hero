<script lang="ts">
	const { selected = false } = $props();

	const strokeWidth = $derived.by(() => {
		return selected ? 2 : 0.9;
	});

	const fill = $derived.by(() => {
		return selected ? '#808000' : '#FFFFFF';
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
	width={selected ? 19 : 23}
	height={selected ? 99 : 103}
	x={selected ? 2 : 0}
	y={selected ? 0 : -2}
/>