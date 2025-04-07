<script lang="ts">
	type Message = 'correct' | 'wrong';
	type MessageItem = {
		message: Message;
		id: number;
	};
	let messages = $state<MessageItem[]>([]);

	export const addMessage = (message: Message) => {
		const id = Math.floor(Math.random() * 1000000);
		const messageItem: MessageItem = { message, id };
		messages.push(messageItem);

		setTimeout(() => {
			messages = messages.filter((msg) => msg.id !== id);
		}, 3000);
	};

	export const clear = () => {
		messages = [];
	};
</script>

<div class="score-flash">
	{#if messages.length > 0}
		{#each messages as message (message.id)}
			<!-- {#key message.id} -->
				<div class="floating-element">
					<p class={message.message}>{message.message == 'correct' ? '+1' : '-3'}</p>
				</div>

		{/each}
	{/if}
</div>

<style>
	.score-flash {
		position: absolute;
		/* top: 150px; */
		bottom: 40px;
		left: 40px;
		font-size: 1.5rem;
		font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
		font-weight: 900;

		.correct {
			color: green;
		}
		.wrong {
			color: red;
		}
	}

	@keyframes flyUp {
		0% {
			transform: translateY(-40px);
			opacity: 1;
		}
		100% {
			transform: translateY(-300px);
			opacity: 0;
		}
	}

	.floating-element {
		position: absolute;
		animation: flyUp 1s ease-in-out forwards;
	}
</style>
