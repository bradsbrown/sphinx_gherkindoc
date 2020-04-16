"""Expected results for feature_to_rst."""

basic_rst = [
    ".. role:: gherkin-step-keyword\n",
    ".. role:: gherkin-step-content\n",
    ".. role:: gherkin-feature-description\n",
    ".. role:: gherkin-scenario-description\n",
    ".. role:: gherkin-feature-keyword\n",
    ".. role:: gherkin-feature-content\n",
    ".. role:: gherkin-background-keyword\n",
    ".. role:: gherkin-background-content\n",
    ".. role:: gherkin-scenario-keyword\n",
    ".. role:: gherkin-scenario-content\n",
    ".. role:: gherkin-scenario-outline-keyword\n",
    ".. role:: gherkin-scenario-outline-content\n",
    ".. role:: gherkin-examples-keyword\n",
    ".. role:: gherkin-examples-content\n",
    ".. role:: gherkin-tag-keyword\n",
    ".. role:: gherkin-tag-content\n",
    "\n",
    ":gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`Testing Sphinx Writer`\n",
    "====================================================================================\n\n",
    "    :gherkin-feature-description:`Test the ability to write Gherkin data to a SphinxWriter object`\n",
    "\n",
    ":gherkin-background-keyword:`Background:` :gherkin-background-content:`Some requirements for this test`\n",
    "-------------------------------------------------------------------------------------------------------\n\n",
    "| :gherkin-step-keyword:`Given` that this file exists\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Test a Scenario`\n",
    "---------------------------------------------------------------------------------\n\n",
    ".. pull-quote::\n\n",
    "    :gherkin-tag-keyword:`Tagged:` quarantined, JIRA-1234\n\n",
    "    :gherkin-scenario-description:`A scenario is quicker to write than a outline but less robust.`\n",
    "\n",
    "| :gherkin-step-keyword:`Given` a test feature\n",
    "| :gherkin-step-keyword:`When` the suite reaches a scenario\n",
    "| :gherkin-step-keyword:`Then` the file is converted into rST\n",
    "\n",
    ":gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`Test a Scenario Outline`\n",
    "-----------------------------------------------------------------------------------------------------------------\n\n",
    "    :gherkin-scenario-description:`A scenario outline helps you avoid confusing duplication.`\n",
    "\n",
    "| :gherkin-step-keyword:`Given` I put **\\<thing\\>** in a blender\n",
    "| :gherkin-step-keyword:`When` I turn the blender on\n",
    "| :gherkin-step-keyword:`Then` it should transform into **\\<other thing\\>**\n",
    "\n",
    ":gherkin-examples-keyword:`Examples:` :gherkin-examples-content:`Fruit`\n",
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n",
    ".. csv-table::\n",
    '    :header: "thing", "other thing"\n',
    "    :quote: “\n\n",
    "    “apple“, “apple sauce“\n",
    "    “banana“, “smoothie“\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Text and Table Scenario`\n",
    "-----------------------------------------------------------------------------------------\n\n",
    "    :gherkin-scenario-description:`Test the additional options for a scenario`\n",
    "\n",
    "| :gherkin-step-keyword:`Given` step text\n",
    "\n",
    "::\n\n",
    "    Lorum ipsum solor sit amet.\n\n",
    "| :gherkin-step-keyword:`When` the suite reaches a scenario table\n",
    "\n",
    "    .. csv-table::\n",
    '        :header: "name", "department"\n',
    "        :quote: “\n\n",
    "        “Barry“, “Beer Cans“\n",
    "        “Pudey“, “Silly Walks“\n",
    "        “Two-Lumps“, “Silly Walks“\n",
    "\n",
    "| :gherkin-step-keyword:`Then` the file is converted into rST\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Normal scenarios with add on steps (And, But)`\n",
    "---------------------------------------------------------------------------------------------------------------\n\n",
    "| :gherkin-step-keyword:`Given` something\n",
    "| :gherkin-step-keyword:`And` something else\n",
    "| :gherkin-step-keyword:`When` something happens\n",
    "| :gherkin-step-keyword:`Then` something happened\n",
    "| :gherkin-step-keyword:`And` something else also happened\n",
    "| :gherkin-step-keyword:`And` another thing happened\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Indentation is ignored when any step in the scenario has text or a table`\n",
    "------------------------------------------------------------------------------------------------------------------------------------------\n\n",
    "| :gherkin-step-keyword:`Given` a step with some text\n",
    "\n",
    "::\n\n",
    "    Here be that said text!\n\n",
    "| :gherkin-step-keyword:`And` an And step with some text too\n",
    "\n",
    "::\n\n",
    "    Hello again!\n\n",
    "| :gherkin-step-keyword:`And` how about a table in there too\n",
    "\n",
    "    .. csv-table::\n",
    '        :header: "position", "name"\n',
    "        :quote: “\n\n",
    "        “first“, “Who“\n",
    "        “second“, “What“\n",
    "        “third“, “I don't know“\n",
    "\n",
    "| :gherkin-step-keyword:`When` the fantasy has ended\n",
    "| :gherkin-step-keyword:`And` all the children are gone\n",
    "| :gherkin-step-keyword:`Then` something deep inside me\n",
    "\n",
    "::\n\n",
    "    Helps me to carry on\n\n",
    "| :gherkin-step-keyword:`And` Encarnaciooooon\n",
    "| :gherkin-step-keyword:`And` doodle-doodle-doodle-doo\n",
    "\n",
]

basic_rst_with_step_url = [
    ".. role:: gherkin-step-keyword\n",
    ".. role:: gherkin-step-content\n",
    ".. role:: gherkin-feature-description\n",
    ".. role:: gherkin-scenario-description\n",
    ".. role:: gherkin-feature-keyword\n",
    ".. role:: gherkin-feature-content\n",
    ".. role:: gherkin-background-keyword\n",
    ".. role:: gherkin-background-content\n",
    ".. role:: gherkin-scenario-keyword\n",
    ".. role:: gherkin-scenario-content\n",
    ".. role:: gherkin-scenario-outline-keyword\n",
    ".. role:: gherkin-scenario-outline-content\n",
    ".. role:: gherkin-examples-keyword\n",
    ".. role:: gherkin-examples-content\n",
    ".. role:: gherkin-tag-keyword\n",
    ".. role:: gherkin-tag-content\n",
    "\n",
    ":gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`Testing Sphinx Writer`\n",
    "====================================================================================\n\n",
    "    :gherkin-feature-description:`Test the ability to write Gherkin data to a SphinxWriter object`\n",
    "\n",
    ":gherkin-background-keyword:`Background:` :gherkin-background-content:`Some requirements for this test`\n",
    "-------------------------------------------------------------------------------------------------------\n\n",
    "| :gherkin-step-keyword:`Given` that this file exists\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Test a Scenario`\n",
    "---------------------------------------------------------------------------------\n\n",
    ".. pull-quote::\n\n",
    "    :gherkin-tag-keyword:`Tagged:` quarantined, JIRA-1234\n\n",
    "    :gherkin-scenario-description:`A scenario is quicker to write than a outline but less robust.`\n",
    "\n",
    "| :gherkin-step-keyword:`Given` `a test feature <https://github.com/jolly-good-toolbelt/sphinx_gherkindoc>`__\n",
    "| :gherkin-step-keyword:`When` the suite reaches a scenario\n",
    "| :gherkin-step-keyword:`Then` the file is converted into rST\n",
    "\n",
    ":gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`Test a Scenario Outline`\n",
    "-----------------------------------------------------------------------------------------------------------------\n\n",
    "    :gherkin-scenario-description:`A scenario outline helps you avoid confusing duplication.`\n",
    "\n",
    "| :gherkin-step-keyword:`Given` I put **\\<thing\\>** in a blender\n",
    "| :gherkin-step-keyword:`When` I turn the blender on\n",
    "| :gherkin-step-keyword:`Then` it should transform into **\\<other thing\\>**\n",
    "\n",
    ":gherkin-examples-keyword:`Examples:` :gherkin-examples-content:`Fruit`\n",
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n",
    ".. csv-table::\n",
    '    :header: "thing", "other thing"\n',
    "    :quote: “\n\n",
    "    “apple“, “apple sauce“\n",
    "    “banana“, “smoothie“\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Text and Table Scenario`\n",
    "-----------------------------------------------------------------------------------------\n\n",
    "    :gherkin-scenario-description:`Test the additional options for a scenario`\n",
    "\n",
    "| :gherkin-step-keyword:`Given` step text\n",
    "\n",
    "::\n\n",
    "    Lorum ipsum solor sit amet.\n\n",
    "| :gherkin-step-keyword:`When` the suite reaches a scenario table\n",
    "\n",
    "    .. csv-table::\n",
    '        :header: "name", "department"\n',
    "        :quote: “\n\n",
    "        “Barry“, “Beer Cans“\n",
    "        “Pudey“, “Silly Walks“\n",
    "        “Two-Lumps“, “Silly Walks“\n",
    "\n",
    "| :gherkin-step-keyword:`Then` the file is converted into rST\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Normal scenarios with add on steps (And, But)`\n",
    "---------------------------------------------------------------------------------------------------------------\n\n",
    "| :gherkin-step-keyword:`Given` something\n",
    "| :gherkin-step-keyword:`And` something else\n",
    "| :gherkin-step-keyword:`When` something happens\n",
    "| :gherkin-step-keyword:`Then` something happened\n",
    "| :gherkin-step-keyword:`And` something else also happened\n",
    "| :gherkin-step-keyword:`And` another thing happened\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Indentation is ignored when any step in the scenario has text or a table`\n",
    "------------------------------------------------------------------------------------------------------------------------------------------\n\n",
    "| :gherkin-step-keyword:`Given` a step with some text\n",
    "\n",
    "::\n\n",
    "    Here be that said text!\n\n",
    "| :gherkin-step-keyword:`And` an And step with some text too\n",
    "\n",
    "::\n\n",
    "    Hello again!\n\n",
    "| :gherkin-step-keyword:`And` how about a table in there too\n",
    "\n",
    "    .. csv-table::\n",
    '        :header: "position", "name"\n',
    "        :quote: “\n\n",
    "        “first“, “Who“\n",
    "        “second“, “What“\n",
    "        “third“, “I don't know“\n",
    "\n",
    "| :gherkin-step-keyword:`When` the fantasy has ended\n",
    "| :gherkin-step-keyword:`And` all the children are gone\n",
    "| :gherkin-step-keyword:`Then` something deep inside me\n",
    "\n",
    "::\n\n",
    "    Helps me to carry on\n\n",
    "| :gherkin-step-keyword:`And` Encarnaciooooon\n",
    "| :gherkin-step-keyword:`And` doodle-doodle-doodle-doo\n",
    "\n",
]

basic_rst_with_integrated_background = [
    ".. role:: gherkin-step-keyword\n",
    ".. role:: gherkin-step-content\n",
    ".. role:: gherkin-feature-description\n",
    ".. role:: gherkin-scenario-description\n",
    ".. role:: gherkin-feature-keyword\n",
    ".. role:: gherkin-feature-content\n",
    ".. role:: gherkin-background-keyword\n",
    ".. role:: gherkin-background-content\n",
    ".. role:: gherkin-scenario-keyword\n",
    ".. role:: gherkin-scenario-content\n",
    ".. role:: gherkin-scenario-outline-keyword\n",
    ".. role:: gherkin-scenario-outline-content\n",
    ".. role:: gherkin-examples-keyword\n",
    ".. role:: gherkin-examples-content\n",
    ".. role:: gherkin-tag-keyword\n",
    ".. role:: gherkin-tag-content\n",
    "\n",
    ":gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`Testing Sphinx Writer`\n",
    "====================================================================================\n\n",
    "    :gherkin-feature-description:`Test the ability to write Gherkin data to a SphinxWriter object`\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Test a Scenario`\n",
    "---------------------------------------------------------------------------------\n\n",
    ".. pull-quote::\n\n",
    "    :gherkin-tag-keyword:`Tagged:` quarantined, JIRA-1234\n\n",
    "    :gherkin-scenario-description:`A scenario is quicker to write than a outline but less robust.`\n",
    "\n",
    "| :gherkin-step-keyword:`Given` that this file exists\n",
    "| :gherkin-step-keyword:`Given` a test feature\n",
    "| :gherkin-step-keyword:`When` the suite reaches a scenario\n",
    "| :gherkin-step-keyword:`Then` the file is converted into rST\n",
    "\n",
    ":gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`Test a Scenario Outline`\n",
    "-----------------------------------------------------------------------------------------------------------------\n\n",
    "    :gherkin-scenario-description:`A scenario outline helps you avoid confusing duplication.`\n",
    "\n",
    "| :gherkin-step-keyword:`Given` that this file exists\n",
    "| :gherkin-step-keyword:`Given` I put **\\<thing\\>** in a blender\n",
    "| :gherkin-step-keyword:`When` I turn the blender on\n",
    "| :gherkin-step-keyword:`Then` it should transform into **\\<other thing\\>**\n",
    "\n",
    ":gherkin-examples-keyword:`Examples:` :gherkin-examples-content:`Fruit`\n",
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n",
    ".. csv-table::\n",
    '    :header: "thing", "other thing"\n',
    "    :quote: “\n\n",
    "    “apple“, “apple sauce“\n",
    "    “banana“, “smoothie“\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Text and Table Scenario`\n",
    "-----------------------------------------------------------------------------------------\n\n",
    "    :gherkin-scenario-description:`Test the additional options for a scenario`\n",
    "\n",
    "| :gherkin-step-keyword:`Given` that this file exists\n",
    "| :gherkin-step-keyword:`Given` step text\n",
    "\n",
    "::\n\n",
    "    Lorum ipsum solor sit amet.\n\n",
    "| :gherkin-step-keyword:`When` the suite reaches a scenario table\n",
    "\n",
    "    .. csv-table::\n",
    '        :header: "name", "department"\n',
    "        :quote: “\n\n",
    "        “Barry“, “Beer Cans“\n",
    "        “Pudey“, “Silly Walks“\n",
    "        “Two-Lumps“, “Silly Walks“\n",
    "\n",
    "| :gherkin-step-keyword:`Then` the file is converted into rST\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Normal scenarios with add on steps (And, But)`\n",
    "---------------------------------------------------------------------------------------------------------------\n\n",
    "| :gherkin-step-keyword:`Given` that this file exists\n",
    "| :gherkin-step-keyword:`Given` something\n",
    "| :gherkin-step-keyword:`And` something else\n",
    "| :gherkin-step-keyword:`When` something happens\n",
    "| :gherkin-step-keyword:`Then` something happened\n",
    "| :gherkin-step-keyword:`And` something else also happened\n",
    "| :gherkin-step-keyword:`And` another thing happened\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Indentation is ignored when any step in the scenario has text or a table`\n",
    "------------------------------------------------------------------------------------------------------------------------------------------\n\n",
    "| :gherkin-step-keyword:`Given` that this file exists\n",
    "| :gherkin-step-keyword:`Given` a step with some text\n",
    "\n",
    "::\n\n",
    "    Here be that said text!\n\n",
    "| :gherkin-step-keyword:`And` an And step with some text too\n",
    "\n",
    "::\n\n",
    "    Hello again!\n\n",
    "| :gherkin-step-keyword:`And` how about a table in there too\n",
    "\n",
    "    .. csv-table::\n",
    '        :header: "position", "name"\n',
    "        :quote: “\n\n",
    "        “first“, “Who“\n",
    "        “second“, “What“\n",
    "        “third“, “I don't know“\n",
    "\n",
    "| :gherkin-step-keyword:`When` the fantasy has ended\n",
    "| :gherkin-step-keyword:`And` all the children are gone\n",
    "| :gherkin-step-keyword:`Then` something deep inside me\n",
    "\n",
    "::\n\n",
    "    Helps me to carry on\n\n",
    "| :gherkin-step-keyword:`And` Encarnaciooooon\n",
    "| :gherkin-step-keyword:`And` doodle-doodle-doodle-doo\n",
    "\n",
]

basic_rst_unique_integrated_background_step_format = [
    ".. role:: gherkin-step-keyword\n",
    ".. role:: gherkin-step-content\n",
    ".. role:: gherkin-feature-description\n",
    ".. role:: gherkin-scenario-description\n",
    ".. role:: gherkin-feature-keyword\n",
    ".. role:: gherkin-feature-content\n",
    ".. role:: gherkin-background-keyword\n",
    ".. role:: gherkin-background-content\n",
    ".. role:: gherkin-scenario-keyword\n",
    ".. role:: gherkin-scenario-content\n",
    ".. role:: gherkin-scenario-outline-keyword\n",
    ".. role:: gherkin-scenario-outline-content\n",
    ".. role:: gherkin-examples-keyword\n",
    ".. role:: gherkin-examples-content\n",
    ".. role:: gherkin-tag-keyword\n",
    ".. role:: gherkin-tag-content\n",
    "\n",
    ":gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`Testing Sphinx Writer`\n",
    "====================================================================================\n\n",
    "    :gherkin-feature-description:`Test the ability to write Gherkin data to a SphinxWriter object`\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Test a Scenario`\n",
    "---------------------------------------------------------------------------------\n\n",
    ".. pull-quote::\n\n",
    "    :gherkin-tag-keyword:`Tagged:` quarantined, JIRA-1234\n\n",
    "    :gherkin-scenario-description:`A scenario is quicker to write than a outline but less robust.`\n",
    "\n",
    "| :gherkin-step-keyword:`Given` that this file exists *(Background)*\n",
    "| :gherkin-step-keyword:`Given` a test feature\n",
    "| :gherkin-step-keyword:`When` the suite reaches a scenario\n",
    "| :gherkin-step-keyword:`Then` the file is converted into rST\n",
    "\n",
    ":gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`Test a Scenario Outline`\n",
    "-----------------------------------------------------------------------------------------------------------------\n\n",
    "    :gherkin-scenario-description:`A scenario outline helps you avoid confusing duplication.`\n",
    "\n",
    "| :gherkin-step-keyword:`Given` that this file exists *(Background)*\n",
    "| :gherkin-step-keyword:`Given` I put **\\<thing\\>** in a blender\n",
    "| :gherkin-step-keyword:`When` I turn the blender on\n",
    "| :gherkin-step-keyword:`Then` it should transform into **\\<other thing\\>**\n",
    "\n",
    ":gherkin-examples-keyword:`Examples:` :gherkin-examples-content:`Fruit`\n",
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n",
    ".. csv-table::\n",
    '    :header: "thing", "other thing"\n',
    "    :quote: “\n\n",
    "    “apple“, “apple sauce“\n",
    "    “banana“, “smoothie“\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Text and Table Scenario`\n",
    "-----------------------------------------------------------------------------------------\n\n",
    "    :gherkin-scenario-description:`Test the additional options for a scenario`\n",
    "\n",
    "| :gherkin-step-keyword:`Given` that this file exists *(Background)*\n",
    "| :gherkin-step-keyword:`Given` step text\n",
    "\n",
    "::\n\n",
    "    Lorum ipsum solor sit amet.\n\n",
    "| :gherkin-step-keyword:`When` the suite reaches a scenario table\n",
    "\n",
    "    .. csv-table::\n",
    '        :header: "name", "department"\n',
    "        :quote: “\n\n",
    "        “Barry“, “Beer Cans“\n",
    "        “Pudey“, “Silly Walks“\n",
    "        “Two-Lumps“, “Silly Walks“\n",
    "\n",
    "| :gherkin-step-keyword:`Then` the file is converted into rST\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Normal scenarios with add on steps (And, But)`\n",
    "---------------------------------------------------------------------------------------------------------------\n\n",
    "| :gherkin-step-keyword:`Given` that this file exists *(Background)*\n",
    "| :gherkin-step-keyword:`Given` something\n",
    "| :gherkin-step-keyword:`And` something else\n",
    "| :gherkin-step-keyword:`When` something happens\n",
    "| :gherkin-step-keyword:`Then` something happened\n",
    "| :gherkin-step-keyword:`And` something else also happened\n",
    "| :gherkin-step-keyword:`And` another thing happened\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Indentation is ignored when any step in the scenario has text or a table`\n",
    "------------------------------------------------------------------------------------------------------------------------------------------\n\n",
    "| :gherkin-step-keyword:`Given` that this file exists *(Background)*\n",
    "| :gherkin-step-keyword:`Given` a step with some text\n",
    "\n",
    "::\n\n",
    "    Here be that said text!\n\n",
    "| :gherkin-step-keyword:`And` an And step with some text too\n",
    "\n",
    "::\n\n",
    "    Hello again!\n\n",
    "| :gherkin-step-keyword:`And` how about a table in there too\n",
    "\n",
    "    .. csv-table::\n",
    '        :header: "position", "name"\n',
    "        :quote: “\n\n",
    "        “first“, “Who“\n",
    "        “second“, “What“\n",
    "        “third“, “I don't know“\n",
    "\n",
    "| :gherkin-step-keyword:`When` the fantasy has ended\n",
    "| :gherkin-step-keyword:`And` all the children are gone\n",
    "| :gherkin-step-keyword:`Then` something deep inside me\n",
    "\n",
    "::\n\n",
    "    Helps me to carry on\n\n",
    "| :gherkin-step-keyword:`And` Encarnaciooooon\n",
    "| :gherkin-step-keyword:`And` doodle-doodle-doodle-doo\n",
    "\n",
]

tags_rst = [
    ".. role:: gherkin-step-keyword\n",
    ".. role:: gherkin-step-content\n",
    ".. role:: gherkin-feature-description\n",
    ".. role:: gherkin-scenario-description\n",
    ".. role:: gherkin-feature-keyword\n",
    ".. role:: gherkin-feature-content\n",
    ".. role:: gherkin-background-keyword\n",
    ".. role:: gherkin-background-content\n",
    ".. role:: gherkin-scenario-keyword\n",
    ".. role:: gherkin-scenario-content\n",
    ".. role:: gherkin-scenario-outline-keyword\n",
    ".. role:: gherkin-scenario-outline-content\n",
    ".. role:: gherkin-examples-keyword\n",
    ".. role:: gherkin-examples-content\n",
    ".. role:: gherkin-tag-keyword\n",
    ".. role:: gherkin-tag-content\n",
    "\n",
    ":gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`Testing Sphinx Writer`\n",
    "====================================================================================\n\n",
    "    :gherkin-feature-description:`Test the ability to write Gherkin data to a SphinxWriter object`\n",
    "\n",
    ":gherkin-background-keyword:`Background:` :gherkin-background-content:`Some requirements for this test`\n",
    "-------------------------------------------------------------------------------------------------------\n\n",
    "| :gherkin-step-keyword:`Given` that this file exists\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Test a Scenario`\n",
    "---------------------------------------------------------------------------------\n\n",
    ".. pull-quote::\n\n",
    "    :gherkin-tag-keyword:`Tagged:` api, tag_with_url (Inherited from Feature: positive )\n\n",
    "    :gherkin-scenario-description:`A scenario is quicker to write than a outline but less robust.`\n",
    "\n",
    "| :gherkin-step-keyword:`Given` a test feature\n",
    "| :gherkin-step-keyword:`When` the suite reaches a scenario\n",
    "| :gherkin-step-keyword:`Then` the file is converted into rST\n",
    "\n",
]

tags_rst_with_urls = [
    ".. role:: gherkin-step-keyword\n",
    ".. role:: gherkin-step-content\n",
    ".. role:: gherkin-feature-description\n",
    ".. role:: gherkin-scenario-description\n",
    ".. role:: gherkin-feature-keyword\n",
    ".. role:: gherkin-feature-content\n",
    ".. role:: gherkin-background-keyword\n",
    ".. role:: gherkin-background-content\n",
    ".. role:: gherkin-scenario-keyword\n",
    ".. role:: gherkin-scenario-content\n",
    ".. role:: gherkin-scenario-outline-keyword\n",
    ".. role:: gherkin-scenario-outline-content\n",
    ".. role:: gherkin-examples-keyword\n",
    ".. role:: gherkin-examples-content\n",
    ".. role:: gherkin-tag-keyword\n",
    ".. role:: gherkin-tag-content\n",
    "\n",
    ":gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`Testing Sphinx Writer`\n",
    "====================================================================================\n\n",
    "    :gherkin-feature-description:`Test the ability to write Gherkin data to a SphinxWriter object`\n",
    "\n",
    ":gherkin-background-keyword:`Background:` :gherkin-background-content:`Some requirements for this test`\n",
    "-------------------------------------------------------------------------------------------------------\n\n",
    "| :gherkin-step-keyword:`Given` that this file exists\n",
    "\n",
    ":gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Test a Scenario`\n",
    "---------------------------------------------------------------------------------\n\n",
    ".. pull-quote::\n\n",
    "    :gherkin-tag-keyword:`Tagged:` api, `tag_with_url <https://github.com/jolly-good-toolbelt/sphinx_gherkindoc>`__ (Inherited from Feature: positive )\n\n",
    "    :gherkin-scenario-description:`A scenario is quicker to write than a outline but less robust.`\n",
    "\n",
    "| :gherkin-step-keyword:`Given` a test feature\n",
    "| :gherkin-step-keyword:`When` the suite reaches a scenario\n",
    "| :gherkin-step-keyword:`Then` the file is converted into rST\n",
    "\n",
]
