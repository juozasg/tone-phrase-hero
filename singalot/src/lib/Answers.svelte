<script lang="ts">
	interface Props {
		answerOnClick: (key: string, mood: 'happy' | 'sad') => void;
	}

	const { answerOnClick }: Props = $props();
</script>

	<div class="answers">
		<!-- C# key -->
		<button class="btn btn-primary" onclick={() => answerOnClick('C#', 'sad')}>Cis moll</button>
		<button class="btn btn-primary" onclick={() => answerOnClick('C#', 'happy')}>Des dur</button>

		<!-- D# key -->
		<button class="btn btn-primary" onclick={() => answerOnClick('D#', 'sad')}>Dis moll</button>
		<button disabled class="btn btn-primary">Es dur</button>

		<!-- F# key -->
		<button disabled class="btn btn-primary">Fis moll</button>
		<button class="btn btn-primary" onclick={() => answerOnClick('F#', 'happy')}>Ges dur</button>

		<!-- G# key -->
		<button class="btn btn-primary" onclick={() => answerOnClick('G#', 'sad')}>Gis moll</button>
		<button class="btn btn-primary" onclick={() => answerOnClick('G#', 'happy')}>As dur</button>

	</div>

<style>

	.btn {
		margin: 3px;
	}
	.answers {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
	}
</style>

