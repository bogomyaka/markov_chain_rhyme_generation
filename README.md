# markov_chain_rhyme_generation
**Возможно, Марковские цепи — не лучший выбор для стихотворений, поскольку они не хранят контекст и генерируют бред, но в этом вся их прелесть :)**

Для генерации предложений использовалась моделька markovify с "привинченным" методом, который генерирует последующее предложение, пока не рифмуются их последние слова. Для поиска рифмы к слову — словарь произношения CMU, в котором собраны фонемы для более чем 134.000 английских слов. 

Из-за того, что последующее предложение генерируется "пока не", время ожидания может быть долгим. По-хорошему также нужно было проверять и количество слогов, но тогда результат ожидался бы еще дольше.
